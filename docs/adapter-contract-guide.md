# 전자계약서비스 (단기 임대차 계약 시스템) 구축 가이드

이 문서는 다음 번에 동일한 전자계약서비스를 0부터 다시 구축할 때 **복사-붙여넣기**만으로 완벽하게 동일한 사이트를 만들 수 있도록 정리된 백업 가이드입니다.

---

## 1. 프로젝트 초기 세팅
```bash
npx create-next-app@latest adapter-contract
# 옵션: TypeScript (Yes), ESLint (Yes), Tailwind CSS (Yes), src/ directory (Yes), App Router (Yes), import alias (No)
cd adapter-contract
npm install @supabase/supabase-js lucide-react react-signature-canvas
npm install -D @types/react-signature-canvas
```

## 2. 데이터베이스 세팅 (Supabase)
Supabase SQL Editor에서 아래 쿼리를 실행하여 contracts 테이블을 생성합니다.
```sql
create table contracts (
  id bigint primary key generated always as identity,
  created_at timestamptz default now(),
  contract_token text not null unique,
  accommodation_name text,
  room_name text,
  check_in_date text,
  check_out_date text,
  deposit_amount text,
  total_amount text,
  special_terms text,
  status text default 'WAITING',
  tenant_name text,
  tenant_phone text,
  tenant_address text,
  tenant_birthday varchar(6),
  signature_image_url text,
  signed_at timestamptz
);
```

## 3. 환경 변수 설정 (.env.local)
프로젝트 루트에 .env.local 파일을 생성하고 Supabase 프로젝트 정보를 입력합니다.
```env
NEXT_PUBLIC_SUPABASE_URL=https://[본인프로젝트].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=[본인프로젝트_ANON_KEY]
```

---

## 4. 핵심 소스 코드 복사/붙여넣기

### `src/app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "전자 임대 계약",
  description: "전자 임대 계약 시스템",
  robots: {
    index: false,
    follow: false,
  },
};

export const viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  colorScheme: 'light',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
      {/* Google Analytics 4 (GA4) */}
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-2N5V6S642H"></script>
      <script
        dangerouslySetInnerHTML={{
          __html: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-2N5V6S642H');
          `,
        }}
      />
{children}</body>
    </html>
  );
}
```

### `src/app/page.tsx`
```typescript
import { redirect } from "next/navigation";

export default function Home() {
  redirect("/admin");
}
```

### `src/app/admin/page.tsx`
```typescript
'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';

export default function AdminDashboard() {
  // 🧭 메뉴 상태 관리 ('dashboard': 에디터, 'status': 진행현황, 'templates': 양식함, 'legal': 법적효력안내)
  const [currentMenu, setCurrentMenu] = useState<'dashboard' | 'status' | 'templates' | 'legal'>('dashboard');
  const [stats, setStats] = useState({ total: 0, pending: 0, signed: 0, sales: 0, totalSales: 0 });
  const [recentContracts, setRecentContracts] = useState<any[]>([]);
  const [loadingStats, setLoadingStats] = useState(true);
  const [savedTemplates, setSavedTemplates] = useState<any[]>([]);

  // 🔒 관리자 인증 상태
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [passwordInput, setPasswordInput] = useState('');
  
  // 🔐 비밀번호 변경 및 보안 질문 모달 상태
  const [showPasswordModal, setShowPasswordModal] = useState(false);
  const [pwChangeInput, setPwChangeInput] = useState({ current: '', new: '', confirm: '' });
  
  const [showSecuritySettingsModal, setShowSecuritySettingsModal] = useState(false);
  const [securitySettingsInput, setSecuritySettingsInput] = useState({ currentPassword: '', question: '', answer: '' });

  const [showResetModal, setShowResetModal] = useState(false);
  const [securityQuestion, setSecurityQuestion] = useState('보안 질문을 불러오는 중...');
  const [resetInput, setResetInput] = useState({ answer: '', newPassword: '', confirmPassword: '' });

  const today = new Date();
  const currentYear = String(today.getFullYear());
  const currentMonth = String(today.getMonth() + 1).padStart(2, '0');
  const currentDay = String(today.getDate()).padStart(2, '0');

  // 📝 주민등록번호 13자리 전체 입력 및 가이드라인 관리를 위한 상태 구조
  const [contractData, setContractData] = useState({
    contract_serial: '',
    contract_name: '표선 게스트하우스 102호',
    main_title: '단기 임대차 계약서',
    main_description: '임대인과 임차인은 아래 부동산에 대한 “단기 시설물 사용”에 관한 임대차 계약을 아래와 같이 체결한다.',
    
    title_article_1: '[제1조] 단기 시설물 사용 부동산의 표시',
    lbl_address: '주 소', address_main: '제주특별자치도 서귀포시 표선면 가시로 349-1, 표선 게스트하우스 102호',
    lbl_rent_part: '임대할부분', rent_part: '독채전체',
    lbl_house_type: '주택유형', house_type: '단독주택',
    lbl_area: '면 적', area_size: '대지 340㎡ / 전용 99㎡',
    
    title_article_2: '[제2조] 계약조건',
    lbl_period: '사용기간', start_year: '2026', start_month: '07', start_day: '01', end_year: '2026', end_month: '07', end_day: '31',
    lbl_deposit: '보증금', deposit: '300,000 원', lbl_premium: '관리비', premium: '0원 (공과금 실비처리)',
    lbl_price: '이용금액', total_amount: '1,500,000 원', lbl_cleaning: '퇴실 청소비', cleaning_fee: '0원',
    
    title_article_3: '[제3조] 대금 지불방식',
    lbl_total: '총액', pay_amount: '1,500,000 원', pay_year: '2026', pay_month: '06', pay_day: '18', lbl_pay_status: '일 지급완료',
    
    title_article_4: '[제4조] 주요 계약 사항',
    article_4: '1. 本 계약의 임차인은 전입신고가 되어 있는 본 거주지가 있고, 일시적으로 단기 사용의 의사를 밝히고 단기임대차 계약을 체결한다.\n2. 本 계약은 단기 사용을 위한 계약으로 전입신고하지 않기로 하며, 주택임대차보호법 4조의 임대차 기간을 적용 받지 않는다.\n3. 임대인은 임실일 전에 해당 부동산의 상태가 양호한지 미리 확인하고 임차인에게 인도 한다.\n4. 임대인은 임차인이 사용 기간 동안 정상적 거주가 가능할 수 있도록 유지보수의 의무가 있다.\n5. 임차인은 사용기간 동안 해당 부동산을 유지관리 하여야 한다. 또한 소모품은 임차인이 교체한다.\n6. 임차인은 퇴실 시 입주상태와 다른 부분(파손, 훼손, 망실 등)이 발생한 경우 원상회복하거나 그 손해를 배상하여야 한다.',
    
    title_article_5: '[제5조] 퇴실 관련사항 약정',
    article_5: '1. 임차인은 이용기간 만료일까지 임차인 소유의 물건과 쓰레기를 깨끗이 치우고 임대인에게 주택을 명도하여야 한다.\n2. 사용만료일이 경과하여 퇴실하지 않으면, 임대인은 별도의 최고나 내용증명 없이 열쇠, 비밀번호 등을 교체하고 단전단수 조치를 할 수 있으며, 임차인은 이에 대한 민, 형사상 어떠한 주장도 할 수 없을 뿐 아니라, 임차인은 임대인이 입은 손해를 배상하여야 한다.\n3. 만료일까지 치우지 못한 임차인 소유의 물건은 임대인이 지정한 보관장소에 보관하기로 하며 이때 발생한 이전비용, 보관비용은 임차인이 지불하기로 한다.\n4. 만료일 5일이내에 해당 물품을 인수 하지 않을 시에는 해당 물품의 소유권을 포기하고 일체의 민, 형사상의 책임을 묻지 않기로 한다.',
    
    title_article_6: '[제6조] 특약 사항',
    special_terms: '모든 공과금(전기, 수도, LPG 가스)은 임차인이 부담하며, 인터넷, TV 등의 사용료는 임대인이 부담한다.',
    
    contract_year: currentYear, contract_month: currentMonth, contract_day: currentDay,
    
    lbl_host_title: '임대인', lbl_host_addr: '주 소', host_address: '제주특별자치도 서귀포시 표선면 가시로 349-10', lbl_host_biz: '사업자번호', host_business_num: '542-98-01816', lbl_host_name: '이 름', host_name: '제주킹덤', lbl_host_phone: '전 화', host_phone: '070-7954-1417',
    lbl_tenant_title: '임차인', lbl_tenant_addr: '주 소', tenant_address: '주소를 입력하세요.', 
    lbl_tenant_birth: '주민등록번호', tenant_birthday: '', 
    lbl_tenant_name: '이 름', tenant_name: '성명 입력', lbl_tenant_phone: '전 화', tenant_phone: '010-0000-0000',
    created_at: '2026-06-19', updated_at: '2026-06-19'
  });

  const [loading, setLoading] = useState(false);
  const [contractUrl, setContractUrl] = useState('');

    // 💡 숫자 앞뒤 텍스트나 날짜가 섞여 있어도 순수 계약 금액만 안전하게 추출하는 파서
  const parseAmount = (val: any): number => {
    if (!val) return 0;
    const str = String(val).trim();
    const match = str.match(/^([0-9,]+)/) || str.match(/([0-9,]+)\s*원/) || str.match(/([0-9,]+)/);
    if (match && match[1]) {
      return parseInt(match[1].replace(/,/g, ''), 10) || 0;
    }
    return parseInt(str.replace(/[^0-9]/g, ''), 10) || 0;
  };

  const loadRealDatabaseData = async () => {
    try {
      const res = await fetch('/api/admin/contracts');
      const json = await res.json();
      if (!json.success) throw new Error(json.message);
      const data = json.data;
      
      if (data) {
        const total = data.length;
        const signedContracts = data.filter((c: any) => c.status === 'SIGNED');
        const signed = signedContracts.length;
        const pending = total - signed;

        // 한국시간(KST, UTC+9) 기준 현재 연도와 월
        const now = new Date();
        const kstOffset = 9 * 60 * 60 * 1000;
        const kstNow = new Date(now.getTime() + kstOffset);
        const currentYear = kstNow.getUTCFullYear();
        const currentMonth = kstNow.getUTCMonth(); // 0 ~ 11

        // 이번 달에 서명 완료(signed_at 우선, 없으면 created_at)된 계약 필터링
        const thisMonthSigned = signedContracts.filter((c: any) => {
          const targetDateStr = c.signed_at || c.created_at;
          if (!targetDateStr) return false;
          const d = new Date(new Date(targetDateStr).getTime() + kstOffset);
          return d.getUTCFullYear() === currentYear && d.getUTCMonth() === currentMonth;
        });

        const thisMonthSales = thisMonthSigned.reduce((sum: number, c: any) => sum + parseAmount(c.total_amount), 0);
        const totalSales = signedContracts.reduce((sum: number, c: any) => sum + parseAmount(c.total_amount), 0);

        setStats({ total, pending, signed, sales: thisMonthSales, totalSales });
        setRecentContracts(data);
      }
    } catch (err) { console.error(err); } finally { setLoadingStats(false); }
  };

      // 🌐 서버 DB에서 마스터 양식(템플릿) 로드 및 각 PC의 로컬 양식 자동 병합(Auto-Merge)
  const loadTemplatesFromDB = async () => {
    try {
      const res = await fetch('/api/admin/templates');
      const json = await res.json();
      const serverTemplates: any[] = (json.success && json.templates) ? json.templates : [];

      // 현재 브라우저의 로컬스토리지에 저장되어 있던 템플릿 확인
      const stored = localStorage.getItem('adapter_contract_templates');
      let localTemplates: any[] = [];
      if (stored) {
        try {
          const parsed = JSON.parse(stored);
          if (Array.isArray(parsed)) localTemplates = parsed;
        } catch (e) {}
      }

      // 서버에 없고 해당 PC 로컬에만 있는 템플릿(예: 다른 PC에서 등록했던 양식) 자동 감지
      const missingInServer = localTemplates.filter(
        (lt: any) => lt.name && !serverTemplates.some((st: any) => st.name.trim() === lt.name.trim())
      );

      let finalTemplates = [...serverTemplates];

      if (missingInServer.length > 0) {
        // 로컬에만 남아있던 양식을 서버 DB로 즉시 자동 동기화하여 영구 보존
        try {
          const syncRes = await fetch('/api/admin/templates', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ bulkTemplates: missingInServer })
          });
          const syncJson = await syncRes.json();
          if (syncJson.success && syncJson.templates) {
            finalTemplates = syncJson.templates;
          } else {
            finalTemplates = [...serverTemplates, ...missingInServer];
          }
        } catch (syncErr) {
          finalTemplates = [...serverTemplates, ...missingInServer];
        }
      }

      if (finalTemplates.length > 0) {
        setSavedTemplates(finalTemplates);
        localStorage.setItem('adapter_contract_templates', JSON.stringify(finalTemplates));
        return finalTemplates;
      }
    } catch (e) {
      console.error('Failed to load templates from server:', e);
    }
    return [];
  };

  useEffect(() => {
    const init = async () => {
      // 1. 서버 DB에서 마스터 양식 불러오기
      const templates = await loadTemplatesFromDB();

      // 2. 최종 작업 중이던 초안 확인
      const savedDraft = localStorage.getItem('adapter_contract_current_draft');
      if (savedDraft) {
        try {
          setContractData(JSON.parse(savedDraft));
        } catch (e) {
          console.error(e);
        }
      } else if (templates && templates.length > 0) {
        setContractData(templates[0].data);
      }
    };
    init();
  }, []);

  useEffect(() => {
    loadRealDatabaseData();
  }, [contractUrl]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const updated = { ...contractData, [e.target.name]: e.target.value };
    setContractData(updated);
    localStorage.setItem('adapter_contract_current_draft', JSON.stringify(updated));
  };

  const handleCreateLink = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setContractUrl('');
    try {
      const res = await fetch('/api/contract', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          acc_name: contractData.contract_name,
          room_name: contractData.rent_part,
          start_date: contractData.start_year + '-' + contractData.start_month + '-' + contractData.start_day,
          end_date: contractData.end_year + '-' + contractData.end_month + '-' + contractData.end_day,
          deposit: contractData.deposit, price: contractData.total_amount, special_terms: JSON.stringify(contractData)
        })
      });
      const data = await res.json();
      if (data.success) {
        setContractUrl(window.location.origin + data.contract_url);
        alert('⚡ 계약서 작성완료 및 전송 링크 생성 완료!');
      }
    } catch (err) { alert('오류가 발생했습니다.'); } finally { setLoading(false); }
  };

    const saveTemplateInline = async () => {
    if (!contractData.contract_name.trim()) return alert('저장할 계약서 이름을 입력해 주세요.');
    const index = savedTemplates.findIndex((t) => t.name === contractData.contract_name.trim());
    let updated = [...savedTemplates];
    const nowStr = new Date().toLocaleDateString();

    let targetData = { ...contractData };
    let templateObj: any = null;

    if (index > -1) {
      targetData.updated_at = nowStr;
      templateObj = { ...updated[index], name: contractData.contract_name.trim(), data: targetData };
      updated[index] = templateObj;
    } else {
      if (savedTemplates.length >= 10) return alert('양식은 최대 10개까지만 저장할 수 있습니다.');
      targetData.created_at = nowStr;
      targetData.updated_at = nowStr;
      templateObj = { id: 'tpl_' + Date.now(), name: contractData.contract_name.trim(), data: targetData };
      updated.push(templateObj);
    }

    // 🌐 서버 DB에 영구 저장 (모든 PC에서 동일하게 실시간 동기화)
    try {
      const res = await fetch('/api/admin/templates', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ template: templateObj })
      });
      const json = await res.json();
      if (!json.success) {
        alert('서버 저장 실패: ' + json.message);
        return;
      }
    } catch (err) {
      console.error(err);
      alert('서버 저장 중 오류가 발생했습니다.');
      return;
    }

    setSavedTemplates(updated);
    localStorage.setItem('adapter_contract_templates', JSON.stringify(updated));
    localStorage.setItem('adapter_contract_current_draft', JSON.stringify(targetData));
    alert('💾 [' + contractData.contract_name + '] 양식이 모든 PC에서 연동되도록 서버에 안전하게 저장되었습니다!');
  };

    const loadTemplate = (templateData: any) => {
    // 🛡️ 템플릿 로드 시 이전 계약자의 주민번호 및 개인정보가 유입되지 않도록 항상 안전하게 초기화
    const sanitized = {
      ...templateData,
      tenant_name: '',
      tenant_phone: '',
      tenant_address: '',
      tenant_birthday: '',
      tenant_birthday_full: '',
      contract_serial: ''
    };
    setContractData(sanitized);
    localStorage.setItem('adapter_contract_current_draft', JSON.stringify(sanitized));
  };

  const deleteTemplate = async (id: string) => {
    if (window.confirm('선택하신 계약서 서식 양식을 영구 삭제하시겠습니까? (모든 PC에서 삭제됩니다)')) {
      try {
        const res = await fetch('/api/admin/templates', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: 'delete', id })
        });
        const json = await res.json();
        if (!json.success) {
          alert('삭제 실패: ' + json.message);
          return;
        }
      } catch (err) {
        alert('삭제 중 오류가 발생했습니다.');
        return;
      }

      const updated = savedTemplates.filter(t => t.id !== id);
      setSavedTemplates(updated);
      localStorage.setItem('adapter_contract_templates', JSON.stringify(updated));
      
      const deletedTemplate = savedTemplates.find(t => t.id === id);
      if (deletedTemplate && contractData.contract_name === deletedTemplate.name) {
        if (updated.length > 0) {
          setContractData(updated[0].data);
          localStorage.setItem('adapter_contract_current_draft', JSON.stringify(updated[0].data));
        } else {
          localStorage.removeItem('adapter_contract_current_draft');
        }
      }
      alert('🗑️ 양식이 성공적으로 삭제되었습니다.');
    }
  };

  const handleDeleteContract = async (id: string, name: string) => {
    if (window.confirm('⚠️ [임차인: ' + name + ']의 계약서 데이터를 영구 삭제하시겠습니까?')) {
      try {
        const res = await fetch('/api/contract/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id })
        });
        const data = await res.json();
        if (data.success) {
          alert('🗑️ 데이터가 성공적으로 영구 삭제되었습니다.');
          loadRealDatabaseData();
        } else {
          alert('삭제 실패: ' + data.message);
        }
      } catch (err) { alert('삭제 중 에러가 발생했습니다.'); }
    }
  };

  // 🔗 고유 카카오톡 전송용 링크 주소를 손쉽게 클립보드에 실시간 재복사하는 유틸 함수
  const copyRowLink = (token: string) => {
    const generatedUrl = window.location.origin + '/sign/' + token;
    navigator.clipboard.writeText(generatedUrl);
    alert('📋 해당 계약서의 카카오톡 전송용 링크 주소가 복사되었습니다.\n원하는 대화창에 바로 붙여넣기(Ctrl+V) 하세요!');
  };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password: passwordInput })
      });
      const data = await res.json();
      if (data.success) {
        setIsAuthenticated(true);
      } else {
        alert(data.message || '비밀번호가 일치하지 않습니다.');
      }
    } catch (err) {
      alert('로그인 중 에러가 발생했습니다.');
    }
  };

  const handleChangePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    if (pwChangeInput.new !== pwChangeInput.confirm) {
      return alert('새 비밀번호와 확인이 일치하지 않습니다.');
    }
    if (pwChangeInput.new.length < 4) {
      return alert('비밀번호는 4자리 이상으로 설정해 주세요.');
    }
    try {
      const res = await fetch('/api/auth/change-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ currentPassword: pwChangeInput.current, newPassword: pwChangeInput.new })
      });
      const data = await res.json();
      if (data.success) {
        alert('비밀번호가 성공적으로 변경되었습니다. 다음 로그인부터 새 비밀번호를 사용해주세요.');
        setShowPasswordModal(false);
        setPwChangeInput({ current: '', new: '', confirm: '' });
      } else {
        alert('변경 실패: ' + data.message);
      }
    } catch (err) {
      alert('비밀번호 변경 중 에러가 발생했습니다.');
    }
  };

  const openResetModal = async () => {
    setShowResetModal(true);
    setResetInput({ answer: '', newPassword: '', confirmPassword: '' });
    try {
      const res = await fetch('/api/auth/security-settings');
      const data = await res.json();
      if (data.success) setSecurityQuestion(data.question);
      else setSecurityQuestion('보안 질문을 불러오지 못했습니다.');
    } catch (e) {
      setSecurityQuestion('네트워크 오류');
    }
  };

  const handleResetPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    if (resetInput.newPassword !== resetInput.confirmPassword) {
      return alert('새 비밀번호와 확인이 일치하지 않습니다.');
    }
    if (resetInput.newPassword.length < 4) {
      return alert('새 비밀번호는 4자리 이상으로 설정해 주세요.');
    }
    try {
      const res = await fetch('/api/auth/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answer: resetInput.answer, newPassword: resetInput.newPassword })
      });
      const data = await res.json();
      if (data.success) {
        alert('비밀번호가 성공적으로 초기화되었습니다! 새 비밀번호로 로그인해주세요.');
        setShowResetModal(false);
      } else {
        alert('초기화 실패: ' + data.message);
      }
    } catch (err) {
      alert('초기화 중 에러가 발생했습니다.');
    }
  };

  const openSecuritySettingsModal = async () => {
    setShowSecuritySettingsModal(true);
    setSecuritySettingsInput({ currentPassword: '', question: '', answer: '' });
    try {
      const res = await fetch('/api/auth/security-settings');
      const data = await res.json();
      if (data.success) setSecuritySettingsInput(prev => ({ ...prev, question: data.question }));
    } catch (e) {}
  };

  const handleUpdateSecuritySettings = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!securitySettingsInput.question || !securitySettingsInput.answer) {
      return alert('보안 질문과 답변을 모두 입력해주세요.');
    }
    try {
      const res = await fetch('/api/auth/security-settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ currentPassword: securitySettingsInput.currentPassword, newQuestion: securitySettingsInput.question, newAnswer: securitySettingsInput.answer })
      });
      const data = await res.json();
      if (data.success) {
        alert('보안 질문과 답변이 안전하게 저장되었습니다!');
        setShowSecuritySettingsModal(false);
      } else {
        alert('저장 실패: ' + data.message);
      }
    } catch (err) {
      alert('저장 중 에러가 발생했습니다.');
    }
  };

  if (!isAuthenticated) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', backgroundColor: '#f0f4f8', fontFamily: 'sans-serif' }}>
        <form onSubmit={handleLogin} style={{ backgroundColor: '#fff', padding: '40px', borderRadius: '12px', boxShadow: '0 4px 15px rgba(0,0,0,0.1)', textAlign: 'center' }}>
          <h2 style={{ margin: '0 0 5px 0', color: '#1e293b', fontSize: '20px' }}>🔒 관리자 로그인</h2>
          <p style={{ color: '#64748b', fontSize: '13px', marginBottom: '25px' }}>인가된 관리자만 접근할 수 있습니다.</p>
          <input type="password" value={passwordInput} onChange={(e) => setPasswordInput(e.target.value)} placeholder="비밀번호 입력" style={{ padding: '12px', width: '250px', border: '1px solid #cbd5e1', borderRadius: '6px', marginBottom: '15px', fontSize: '14px', outline: 'none' }} required />
          <button type="submit" style={{ display: 'block', width: '100%', padding: '12px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '14px', marginBottom: '15px' }}>접속하기</button>
          <button type="button" onClick={openResetModal} style={{ display: 'block', width: '100%', padding: '10px', backgroundColor: 'transparent', color: '#64748b', border: 'none', cursor: 'pointer', fontSize: '13px', textDecoration: 'underline' }}>비밀번호를 잊으셨나요?</button>
        </form>

        {showResetModal && (
          <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
            <div style={{ backgroundColor: '#fff', padding: '30px', borderRadius: '12px', width: '350px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
              <h3 style={{ margin: '0 0 15px 0', fontSize: '18px', color: '#0f172a' }}>🛡️ 비밀번호 초기화</h3>
              <p style={{ fontSize: '13px', color: '#64748b', marginBottom: '20px', lineHeight: '1.5' }}>설정하신 보안 질문에 답을 맞히면<br/>비밀번호를 새로 설정할 수 있습니다.</p>
              
              <form onSubmit={handleResetPassword}>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 'bold', color: '#475569', marginBottom: '5px' }}>질문: {securityQuestion}</label>
                  <input type="text" placeholder="답변을 입력하세요" value={resetInput.answer} onChange={(e) => setResetInput({...resetInput, answer: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '15px' }}>
                  <input type="password" placeholder="새 비밀번호 (4자리 이상)" value={resetInput.newPassword} onChange={(e) => setResetInput({...resetInput, newPassword: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '25px' }}>
                  <input type="password" placeholder="새 비밀번호 확인" value={resetInput.confirmPassword} onChange={(e) => setResetInput({...resetInput, confirmPassword: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ display: 'flex', gap: '10px' }}>
                  <button type="button" onClick={() => setShowResetModal(false)} style={{ flex: 1, padding: '10px', backgroundColor: '#f1f5f9', color: '#475569', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>취소</button>
                  <button type="submit" style={{ flex: 1, padding: '10px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>초기화 진행</button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f0f4f8', fontFamily: 'sans-serif', display: 'flex', flexDirection: 'column' }}>
      
      {/* 🧭 상단 메뉴바 헤더 네비게이션 */}
      <div style={{ backgroundColor: '#1e293b', color: '#fff', padding: '0 30px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', height: '65px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)', position: 'sticky', top: 0, zIndex: 100 }}>
        <div style={{ fontSize: '18px', fontWeight: 'bold', color: '#38bdf8', cursor: 'pointer' }} onClick={() => setCurrentMenu('dashboard')}>
          제주모도 전자계약 시스템
        </div>
        <div style={{ display: 'flex', gap: '5px', height: '100%' }}>
          <button onClick={() => setCurrentMenu('dashboard')} style={{ padding: '0 20px', border: 'none', background: currentMenu === 'dashboard' ? '#334155' : 'transparent', color: '#fff', fontSize: '14px', fontWeight: 'bold', cursor: 'pointer', borderBottom: currentMenu === 'dashboard' ? '4px solid #38bdf8' : 'none' }}>계약 발급 에디터</button>
          <button onClick={() => setCurrentMenu('status')} style={{ padding: '0 20px', border: 'none', background: currentMenu === 'status' ? '#334155' : 'transparent', color: '#fff', fontSize: '14px', fontWeight: 'bold', cursor: 'pointer', borderBottom: currentMenu === 'status' ? '4px solid #38bdf8' : 'none' }}>📋 계약 진행 현황 ({stats.total}건)</button>
          <button onClick={() => setCurrentMenu('templates')} style={{ padding: '0 20px', border: 'none', background: currentMenu === 'templates' ? '#334155' : 'transparent', color: '#fff', fontSize: '14px', fontWeight: 'bold', cursor: 'pointer', borderBottom: currentMenu === 'templates' ? '4px solid #38bdf8' : 'none' }}>💾 계약서 양식 저장소 ({savedTemplates.length}/10)</button>
          <button onClick={() => setCurrentMenu('legal')} style={{ padding: '0 20px', border: 'none', background: currentMenu === 'legal' ? '#334155' : 'transparent', color: '#fff', fontSize: '14px', fontWeight: 'bold', cursor: 'pointer', borderBottom: currentMenu === 'legal' ? '4px solid #38bdf8' : 'none' }}>⚖️ 법적 효력 및 지침 안내</button>
          <button onClick={openSecuritySettingsModal} style={{ marginLeft: '15px', padding: '0 15px', border: '1px solid #64748b', background: '#334155', color: '#cbd5e1', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer', borderRadius: '4px', height: '32px', alignSelf: 'center' }}>🛡️ 보안 질문 설정</button>
          <button onClick={() => setShowPasswordModal(true)} style={{ marginLeft: '8px', padding: '0 15px', border: '1px solid #64748b', background: '#334155', color: '#cbd5e1', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer', borderRadius: '4px', height: '32px', alignSelf: 'center' }}>🔒 비밀번호 변경</button>
        </div>
      </div>

      {/* 메인 대시보드 구조 구획 */}
      <div style={{ flex: 1, padding: '30px', maxWidth: '1440px', width: '100%', margin: '0 auto', boxSizing: 'border-box' }}>
        
        {/* 상단 통합 현황 정산 스코어보드 */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '20px', marginBottom: '30px' }}>
          <div style={{ background: '#fff', padding: '18px 25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.02)' }}><div style={{ fontSize: '13px', color: '#6b7280', fontWeight: 'bold' }}>총 계약 건수</div><div style={{ fontSize: '28px', fontWeight: 'bold', color: '#1e293b', marginTop: '4px' }}>{stats.total}건</div></div>
          <div style={{ background: '#fff', padding: '18px 25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.02)' }}><div style={{ fontSize: '13px', color: '#3b82f6', fontWeight: 'bold' }}>⏳ 대기중인 계약</div><div style={{ fontSize: '26px', fontWeight: 'bold', color: '#3b82f6', marginTop: '4px' }}>{stats.pending}건</div></div>
          <div style={{ background: '#fff', padding: '18px 25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.02)' }}><div style={{ fontSize: '13px', color: '#10b981', fontWeight: 'bold' }}>완료된 계약</div><div style={{ fontSize: '26px', fontWeight: 'bold', color: '#10b981', marginTop: '4px' }}>{stats.signed}건</div></div>
          <div style={{ background: '#fff', padding: '18px 25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.02)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ fontSize: '13px', color: '#111827', fontWeight: 'bold' }}>이번 달 정산 매출 ({today.getMonth() + 1}월)</div>
              <span style={{ fontSize: '11px', color: '#64748b' }}>누적 {stats.totalSales.toLocaleString()}원</span>
            </div>
            <div style={{ fontSize: '26px', fontWeight: 'bold', color: '#0f172a', marginTop: '4px' }}>{stats.sales.toLocaleString()}원</div>
          </div>
        </div>

        {/* ===================== [메뉴 1: 계약 발급 에디터 모드] ===================== */}
        {currentMenu === 'dashboard' && (
          <div style={{ display: 'flex', gap: '30px', alignItems: 'flex-start' }}>
            
            {/* 왼쪽 영역: 실물 서식 기반의 양식 에디터 플레이스 (공지박스는 법적효력 탭으로 안전하게 이동됨) */}
            <div style={{ width: 'calc(100% - 480px)', backgroundColor: '#fff', padding: '40px 35px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.04)', border: '1px solid #e2e8f0', boxSizing: 'border-box' }}>

              {/* 계약서 이름 관리 필드 */}
              <div style={{ display: 'flex', gap: '10px', background: '#f8fafc', padding: '15px', borderRadius: '8px', border: '1px solid #cbd5e1', marginBottom: '25px', alignItems: 'center' }}>
                <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#1e293b', whiteSpace: 'nowrap' }}>■ 계약서 이름 :</span>
                <input type="text" name="contract_name" value={contractData.contract_name} onChange={handleInputChange} style={{ flex: 1, padding: '8px 12px', fontSize: '13px', border: '1px solid #cbd5e1', borderRadius: '4px', fontWeight: 'bold' }} />
                <button type="button" onClick={saveTemplateInline} style={{ backgroundColor: '#10b981', color: '#fff', padding: '8px 16px', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold', fontSize: '13px', whiteSpace: 'nowrap' }}>현재 양식함에 저장/업데이트</button>
              </div>

              {/* 가로 휠 스크롤 제어 피커 트랙 */}
              <div style={{ marginBottom: '25px', width: '100%' }}>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#64748b', marginBottom: '6px' }}>📂 마스터 양식 고속 선택 피커 (좌우 마우스 휠/터치 스크롤)</div>
                <div style={{ display: 'flex', gap: '8px', overflowX: 'scroll', paddingBottom: '12px', width: '100%', boxSizing: 'border-box', overflowY: 'hidden' }}>
                  {savedTemplates.length === 0 ? (
                    <span style={{ fontSize: '12px', color: '#94a3b8', fontStyle: 'italic' }}>*저장된 마스터 양식이 없습니다.</span>
                  ) : (
                    savedTemplates.map((tpl) => (
                      <button key={tpl.id} type="button" onClick={() => loadTemplate(tpl.data)} style={{ display: 'inline-block', padding: '8px 16px', backgroundColor: contractData.contract_name === tpl.name ? '#e0f2fe' : '#f1f5f9', border: contractData.contract_name === tpl.name ? '1px solid #0284c7' : '1px solid #cbd5e1', borderRadius: '20px', fontSize: '12.5px', color: contractData.contract_name === tpl.name ? '#0369a1' : '#334155', fontWeight: 'bold', cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0 }}>
                        {tpl.name}
                      </button>
                    ))
                  )}
                </div>
              </div>

              {/* 신규 링크 발급 창 알림 오버레이 */}
              {contractUrl && (
                <div style={{ marginBottom: '25px', padding: '15px', background: '#e0f2fe', borderRadius: '8px', fontSize: '13px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontWeight: 'bold', color: '#0369a1' }}>🎉 전송 링크:</span> 
                  <input type="text" value={contractUrl} readOnly style={{ flex: 1, padding: '4px', border: '1px solid #cbd5e1' }} />
                  <button onClick={() => { navigator.clipboard.writeText(contractUrl); alert('복사완료!'); }} style={{ background: '#0284c7', color: '#fff', border: 'none', padding: '6px 12px', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>주소 복사</button>
                </div>
              )}

              {/* 실물 서식 구조 빌딩 */}
              <div style={{ position: 'relative' }}>
                <div style={{ position: 'absolute', top: '0', right: '0', fontSize: '11px', color: '#64748b', fontFamily: 'monospace' }}>
                  {contractData.contract_serial || '발급 시 자동부여'}
                </div>
                <div style={{ textAlign: 'center', marginBottom: '6px' }}><input type="text" name="main_title" value={contractData.main_title} onChange={handleInputChange} style={{ fontSize: '26px', fontWeight: 'bold', textAlign: 'center', border: '1px dashed #cbd5e1', width: '80%', padding: '4px', letterSpacing: '4px' }} /></div>
              </div>
              <div style={{ textAlign: 'center', marginBottom: '35px' }}><input type="text" name="main_description" value={contractData.main_description} onChange={handleInputChange} style={{ fontSize: '12px', color: '#6b7280', textAlign: 'center', border: '1px dashed #cbd5e1', width: '90%', padding: '4px' }} /></div>

              {/* 제1조 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_1" value={contractData.title_article_1} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '20px', fontSize: '12px' }}>
                <tbody>
                  <tr>
                    <td style={{ width: '95px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}><input type="text" name="lbl_address" value={contractData.lbl_address} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td colSpan={5} style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="address_main" value={contractData.address_main} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                  <tr>
                    <td style={{ border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_rent_part" value={contractData.lbl_rent_part} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="rent_part" value={contractData.rent_part} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ width: '75px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_house_type" value={contractData.lbl_house_type} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="house_type" value={contractData.house_type} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ width: '55px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_area" value={contractData.lbl_area} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="area_size" value={contractData.area_size} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                </tbody>
              </table>

              {/* 제2조 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_2" value={contractData.title_article_2} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '20px', fontSize: '12px' }}>
                <tbody>
                  <tr>
                    <td style={{ width: '95px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_period" value={contractData.lbl_period} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td colSpan={3} style={{ border: '1px solid #000', padding: '8px' }}>
                      <input type="text" name="start_year" value={contractData.start_year} onChange={handleInputChange} style={{ width: '35px', textAlign: 'center', border: 'none' }} />년{' '}
                      <input type="text" name="start_month" value={contractData.start_month} onChange={handleInputChange} style={{ width: '22px', textAlign: 'center', border: 'none' }} />월{' '}
                      <input type="text" name="start_day" value={contractData.start_day} onChange={handleInputChange} style={{ width: '22px', textAlign: 'center', border: 'none' }} />일 ~{' '}
                      <input type="text" name="end_year" value={contractData.end_year} onChange={handleInputChange} style={{ width: '35px', textAlign: 'center', border: 'none' }} />년{' '}
                      <input type="text" name="end_month" value={contractData.end_month} onChange={handleInputChange} style={{ width: '22px', textAlign: 'center', border: 'none' }} />월{' '}
                      <input type="text" name="end_day" value={contractData.end_day} onChange={handleInputChange} style={{ width: '22px', textAlign: 'center', border: 'none' }} />일
                    </td>
                  </tr>
                  <tr>
                    <td style={{ border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_deposit" value={contractData.lbl_deposit} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="deposit" value={contractData.deposit} onChange={handleInputChange} style={{ width: '95%', border: 'none' }} /></td>
                    <td style={{ width: '95px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_premium" value={contractData.lbl_premium} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="premium" value={contractData.premium} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                  <tr>
                    <td style={{ border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_price" value={contractData.lbl_price} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="total_amount" value={contractData.total_amount} onChange={handleInputChange} style={{ width: '95%', border: 'none', fontWeight: 'bold' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', textAlign: 'center', fontWeight: 'bold' }}><input type="text" name="lbl_cleaning" value={contractData.lbl_cleaning} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}><input type="text" name="cleaning_fee" value={contractData.cleaning_fee} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                </tbody>
              </table>

              {/* 제3조 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_3" value={contractData.title_article_3} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '25px', fontSize: '12px' }}>
                <tbody>
                  <tr>
                    <td style={{ width: '95px', border: '1px solid #000', padding: '8px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}><input type="text" name="lbl_total" value={contractData.lbl_total} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '8px' }}>
                      <input type="text" name="pay_amount" value={contractData.pay_amount} onChange={handleInputChange} style={{ width: '130px', border: 'none', fontWeight: 'bold' }} />
                      <input type="text" name="pay_year" value={contractData.pay_year} onChange={handleInputChange} style={{ width: '35px', border: 'none', textAlign: 'center' }} />년{' '}
                      <input type="text" name="pay_month" value={contractData.pay_month} onChange={handleInputChange} style={{ width: '22px', border: 'none', textAlign: 'center' }} />월{' '}
                      <input type="text" name="pay_day" value={contractData.pay_day} onChange={handleInputChange} style={{ width: '22px', border: 'none', textAlign: 'center' }} />
                      <input type="text" name="lbl_pay_status" value={contractData.lbl_pay_status} onChange={handleInputChange} style={{ width: '80px', border: 'none' }} />
                    </td>
                  </tr>
                </tbody>
              </table>

              {/* 제4조 주요 계약 사항 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_4" value={contractData.title_article_4} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <textarea name="article_4" value={contractData.article_4} onChange={handleInputChange} rows={6} style={{ width: '100%', padding: '10px', border: '1px solid #000', fontSize: '12px', marginBottom: '15px', lineHeight: '1.6' }} />
              
              {/* 제5조 퇴실 관련사항 약정 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_5" value={contractData.title_article_5} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <textarea name="article_5" value={contractData.article_5} onChange={handleInputChange} rows={6} style={{ width: '100%', padding: '10px', border: '1px solid #000', fontSize: '12px', marginBottom: '15px', lineHeight: '1.6' }} />
              
              {/* 제6조 특약 사항 */}
              <h4 style={{ margin: '0 0 8px 0' }}><input type="text" name="title_article_6" value={contractData.title_article_6} onChange={handleInputChange} style={{ width: '100%', fontWeight: 'bold', fontSize: '13px', border: 'none', background: 'transparent' }} /></h4>
              <textarea name="special_terms" value={contractData.special_terms} onChange={handleInputChange} rows={3} style={{ width: '100%', padding: '10px', border: '1px solid #000', fontSize: '12px', marginBottom: '20px', lineHeight: '1.6' }} />

              <div style={{ textAlign: 'center', fontSize: '14px', fontWeight: 'bold', margin: '30px 0 15px' }}>
                <input 
                  type="text" 
                  name="contract_year" 
                  value={contractData.contract_year} 
                  onChange={handleInputChange} 
                  style={{ width: '55px', border: '1px dashed #94a3b8', background: '#f8fafc', padding: '2px 4px', borderRadius: '4px', textAlign: 'center', fontWeight: 'bold', fontSize: '14px', outline: 'none' }} 
                />년{' '}
                <input 
                  type="text" 
                  name="contract_month" 
                  value={contractData.contract_month} 
                  onChange={handleInputChange} 
                  style={{ width: '35px', border: '1px dashed #94a3b8', background: '#f8fafc', padding: '2px 4px', borderRadius: '4px', textAlign: 'center', fontWeight: 'bold', fontSize: '14px', outline: 'none' }} 
                />월{' '}
                <input 
                  type="text" 
                  name="contract_day" 
                  value={contractData.contract_day} 
                  onChange={handleInputChange} 
                  style={{ width: '35px', border: '1px dashed #94a3b8', background: '#f8fafc', padding: '2px 4px', borderRadius: '4px', textAlign: 'center', fontWeight: 'bold', fontSize: '14px', outline: 'none' }} 
                />일
              </div>

              {/* 명세 명부 격자판 */}
              <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '25px', fontSize: '12px' }}>
                <tbody>
                  <tr>
                    <td rowSpan={2} style={{ width: '45px', border: '1px solid #000', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}><input type="text" name="lbl_host_title" value={contractData.lbl_host_title} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ width: '75px', border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_host_addr" value={contractData.lbl_host_addr} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="host_address" value={contractData.host_address} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ width: '65px', border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_host_name" value={contractData.lbl_host_name} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="host_name" value={contractData.host_name} onChange={handleInputChange} style={{ width: '100%', border: 'none', fontWeight: 'bold' }} /></td>
                  </tr>
                  <tr>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_host_biz" value={contractData.lbl_host_biz} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="host_business_num" value={contractData.host_business_num} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_host_phone" value={contractData.lbl_host_phone} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="host_phone" value={contractData.host_phone} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                  <tr>
                    <td rowSpan={2} style={{ width: '45px', border: '1px solid #000', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}><input type="text" name="lbl_tenant_title" value={contractData.lbl_tenant_title} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', fontWeight: 'bold', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_tenant_addr" value={contractData.lbl_tenant_addr} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="tenant_address" value={contractData.tenant_address} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_tenant_name" value={contractData.lbl_tenant_name} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="tenant_name" value={contractData.tenant_name} onChange={handleInputChange} style={{ width: '100%', border: 'none', fontWeight: 'bold' }} /></td>
                  </tr>
                  <tr>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_tenant_birth" value={contractData.lbl_tenant_birth} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    {/* 주민등록번호 13자리 텍스트 인풋 플레이스홀더 제어 */}
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="tenant_birthday" value={contractData.tenant_birthday} onChange={handleInputChange} placeholder="880101-1234567" style={{ width: '100%', border: 'none' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', textAlign: 'center' }}><input type="text" name="lbl_tenant_phone" value={contractData.lbl_tenant_phone} onChange={handleInputChange} style={{ width: '100%', border: 'none', textAlign: 'center', background: 'transparent' }} /></td>
                    <td style={{ border: '1px solid #000', padding: '4px' }}><input type="text" name="tenant_phone" value={contractData.tenant_phone} onChange={handleInputChange} style={{ width: '100%', border: 'none' }} /></td>
                  </tr>
                </tbody>
              </table>

              <button onClick={handleCreateLink} style={{ width: '100%', backgroundColor: '#0284c7', color: '#fff', padding: '16px', border: 'none', borderRadius: '6px', fontSize: '15px', fontWeight: 'bold', cursor: 'pointer' }}>
                계약서 작성완료 및 전송 링크 생성
              </button>
            </div>

            {/* 📋 오른쪽 고정형 실시간 모니터링 현황판 (카톡 전송링크 복사용 [링크] 단추 기본 유지) */}
            <div style={{ width: '450px', backgroundColor: '#fff', padding: '20px', borderRadius: '12px', border: '1px solid #e2e8f0', flexShrink: 0 }}>
              <h3 style={{ margin: '0 0 15px 0', fontSize: '14px', fontWeight: 'bold', color: '#1e293b' }}>📋 전자계약 실시간 모니터링 현황</h3>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', tableLayout: 'fixed' }}>
                <thead>
                  <tr style={{ borderBottom: '2px solid #e2e8f0', backgroundColor: '#f8fafc' }}>
                    <th style={{ padding: '8px 4px', textAlign: 'left', width: '20%' }}>임차인</th>
                    <th style={{ padding: '8px 4px', textAlign: 'left', width: '38%' }}>계약서 이름</th>
                    <th style={{ padding: '8px 4px', textAlign: 'left', width: '22%' }}>사용 기간</th>
                    <th style={{ padding: '8px 2px', textAlign: 'center', width: '20%' }}>액션 제어</th>
                  </tr>
                </thead>
                <tbody>
                  {recentContracts.slice(0, 8).map((item, index) => {
                    let details: any = {}; try { details = typeof item.special_terms === 'string' ? JSON.parse(item.special_terms) : (item.special_terms || {}); } catch(e){}
                    const cName = details.contract_name || item.accommodation_name || '일반 계약서';
                    const tName = item.tenant_name || details.tenant_name || '미입력';
                    return (
                      <tr key={index} style={{ borderBottom: '1px solid #f1f5f9' }}>
                        <td style={{ padding: '10px 4px', fontWeight: 'bold', verticalAlign: 'middle' }}>{tName}</td>
                        <td style={{ padding: '10px 4px', verticalAlign: 'middle' }}>
                          <div style={{ wordBreak: 'break-all', whiteSpace: 'normal', lineHeight: '1.4', color: '#0284c7', fontWeight: 'bold' }}>
                            {cName}
                          </div>
                        </td>
                        <td style={{ padding: '10px 4px', color: '#475569', fontSize: '11px', whiteSpace: 'nowrap', verticalAlign: 'middle' }}>
                          {details.start_month || '00'}/{details.start_day || '00'} ~ {details.end_month || '00'}/{details.end_day || '00'}
                        </td>
                        <td style={{ padding: '10px 2px', textAlign: 'center', verticalAlign: 'middle', whiteSpace: 'nowrap' }}>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', color: item.status === 'SIGNED' ? '#16a34a' : '#ea580c', display: 'block', marginBottom: '4px' }}>
                            {item.status === 'SIGNED' ? '완료' : '대기'}
                          </span>
                          <button onClick={() => window.open('/sign/' + item.contract_token, '_blank')} style={{ padding: '1px 3px', backgroundColor: '#475569', color: '#fff', border: 'none', borderRadius: '3px', cursor: 'pointer', fontSize: '10px', marginRight: '2px' }}>보기</button>
                          <button onClick={() => copyRowLink(item.contract_token)} style={{ padding: '1px 3px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '3px', cursor: 'pointer', fontSize: '10px', marginRight: '2px', fontWeight: 'bold' }}>링크</button>
                          <button onClick={() => handleDeleteContract(item.id, tName)} style={{ padding: '1px 3px', backgroundColor: '#ef4444', color: '#fff', border: 'none', borderRadius: '3px', cursor: 'pointer', fontSize: '10px' }}>삭제</button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* ===================== [메뉴 2: 계약 진행 현황 전체 테이블] ===================== */}
        {currentMenu === 'status' && (
          <div style={{ backgroundColor: '#fff', padding: '25px', borderRadius: '12px', border: '1px solid #e2e8f0', overflowX: 'auto' }}>
            <h3 style={{ margin: '0 0 20px 0', fontSize: '16px', fontWeight: 'bold', color: '#1e293b' }}>📋 전체 전자계약 실시간 전송 및 체결 정보</h3>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', minWidth: '1250px' }}>
              <thead>
                <tr style={{ backgroundColor: '#f8fafc', borderBottom: '2px solid #e2e8f0', color: '#475569' }}>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '80px' }}>임차인명</th>
                  <th style={{ padding: '12px 8px', textAlign: 'center', width: '100px' }}>문서번호</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '130px' }}>계약서 이름</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '190px' }}>계약서 주소지</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '140px' }}>사용 기간 전체</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '120px' }}>주민등록번호</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '110px' }}>임차인 연락처</th>
                  <th style={{ padding: '12px 8px', textAlign: 'left', width: '150px' }}>임차인 주소</th>
                  <th style={{ padding: '12px 8px', textAlign: 'center', width: '90px' }}>계약 작성일</th>
                  <th style={{ padding: '12px 8px', textAlign: 'center', width: '110px' }}>상태 및 서명일자</th>
                  <th style={{ padding: '12px 8px', textAlign: 'center', width: '140px' }}>실물출력 및 전송 제어</th>
                </tr>
              </thead>
              <tbody>
                {recentContracts.map((item, index) => {
                  let details: any = {}; try { details = typeof item.special_terms === 'string' ? JSON.parse(item.special_terms) : (item.special_terms || {}); } catch(e){}
                  return (
                    <tr key={index} style={{ borderBottom: '1px solid #f1f5f9' }}>
                      <td style={{ padding: '12px 8px', fontWeight: 'bold' }}>{item.tenant_name || details.tenant_name || '미입력'}</td>
                      <td style={{ padding: '12px 8px', textAlign: 'center', color: '#475569', fontSize: '11px', fontFamily: 'monospace' }}>{details.contract_serial || '-'}</td>
                      <td style={{ padding: '12px 8px', color: '#0284c7', fontWeight: 'bold' }}>{details.contract_name || '일반 양식'}</td>
                      <td style={{ padding: '12px 8px', verticalAlign: 'middle' }}><div style={{ wordBreak: 'break-all', whiteSpace: 'normal', lineHeight: '1.4' }}>{details.address_main || item.address_main}</div></td>
                      <td style={{ padding: '12px 8px', color: '#1e293b', fontWeight: '500' }}>
                        {details.start_year || '2026'}.{details.start_month || '00'}.{details.start_day || '00'} ~<br/>
                        {details.end_year || '2026'}.{details.end_month || '00'}.{details.end_day || '00'}
                      </td>
                      <td style={{ padding: '12px 8px', color: '#475569', fontFamily: 'monospace', fontWeight: 'bold', fontSize: '13px' }}>
                        {(() => {
                          const bday = details.tenant_birthday_full || item.tenant_birthday || details.tenant_birthday;
                          return bday 
                            ? (bday.length === 13 ? bday.substring(0,6) + '-' + bday.substring(6) : bday) 
                            : '미입력';
                        })()}
                      </td>
                      <td style={{ padding: '12px 8px' }}>{item.tenant_phone || details.tenant_phone || '미입력'}</td>
                      <td style={{ padding: '12px 8px', verticalAlign: 'middle' }}><div style={{ wordBreak: 'break-all', whiteSpace: 'normal', lineHeight: '1.4' }}>{item.tenant_address || details.tenant_address || '미입력'}</div></td>
                      <td style={{ padding: '12px 8px', textAlign: 'center', color: '#475569' }}>
                        {item.created_at ? new Date(item.created_at).toLocaleDateString() : '2026.06.19'}
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <div style={{ fontWeight: 'bold', color: item.status === 'SIGNED' ? '#16a34a' : '#ea580c' }}>{item.status === 'SIGNED' ? '✍️ 서명체결완료' : '⏳ 대기중'}</div>
                        {item.signed_at && <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px' }}>{new Date(item.signed_at).toLocaleString()}</div>}
                      </td>
                      <td style={{ padding: '12px 4px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                        <button onClick={() => window.open('/sign/' + item.contract_token, '_blank')} style={{ padding: '4px 6px', backgroundColor: '#1e293b', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold', fontSize: '11px', marginRight: '3px' }}>실물확인</button>
                        <button onClick={() => copyRowLink(item.contract_token)} style={{ padding: '4px 6px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold', fontSize: '11px', marginRight: '3px' }}>링크복사</button>
                        <button onClick={() => handleDeleteContract(item.id, item.tenant_name)} style={{ padding: '4px 4px', backgroundColor: '#ef4444', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '11px' }}>삭제</button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}

        {/* ===================== [메뉴 3: 양식 아카이브 모드] ===================== */}
        {currentMenu === 'templates' && (
          <div style={{ backgroundColor: '#fff', padding: '25px', borderRadius: '12px', border: '1px solid #e2e8f0' }}>
            <h3 style={{ margin: '0 0 5px 0', fontSize: '16px', fontWeight: 'bold', color: '#1e293b' }}>💾 마스터 계약서 양식 저장 아카이브</h3>
            <p style={{ color: '#6b7280', fontSize: '12.5px', margin: '0 0 25px 0' }}>*계약서 발급 에디터 상단에서 간편하게 등록 및 관리하세요. (최대 10개)</p>

            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
              <thead>
                <tr style={{ backgroundColor: '#f8fafc', borderBottom: '2px solid #e2e8f0', color: '#475569' }}>
                  <th style={{ padding: '10px', textAlign: 'left', width: '22%' }}>계약서 이름</th>
                  <th style={{ padding: '10px', textAlign: 'left', width: '30%' }}>계약서 주소</th>
                  <th style={{ padding: '10px', textAlign: 'left', width: '15%' }}>임대인 정보 (상호)</th>
                  <th style={{ padding: '10px', textAlign: 'center', width: '10%' }}>작성일자</th>
                  <th style={{ padding: '10px', textAlign: 'center', width: '10%' }}>수정일자</th>
                  <th style={{ padding: '10px', textAlign: 'center', width: '13%' }}>양식 관리 제어</th>
                </tr>
              </thead>
              <tbody>
                {savedTemplates.map((tpl) => (
                  <tr key={tpl.id} style={{ borderBottom: '1px solid #f1f5f9' }}>
                    <td style={{ padding: '12px 10px', fontWeight: 'bold', color: '#0f172a' }}>{tpl.name}</td>
                    <td style={{ padding: '12px 10px', color: '#334155' }}>{tpl.data.address_main}</td>
                    <td style={{ padding: '12px 10px' }}>{tpl.data.host_name}</td>
                    <td style={{ padding: '12px 10px', textAlign: 'center', color: '#64748b', fontSize: '12px' }}>{tpl.data.created_at || '2026.06.19'}</td>
                    <td style={{ padding: '12px 10px', textAlign: 'center', color: '#64748b', fontSize: '12px' }}>{tpl.data.updated_at || '2026.06.19'}</td>
                    <td style={{ padding: '12px 6px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                      <button onClick={() => { loadTemplate(tpl.data); setCurrentMenu('dashboard'); alert('🔄 양식이 에디터에 로드되었습니다.'); }} style={{ padding: '4px 8px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold', fontSize: '11px', marginRight: '3px' }}>선택(로드)</button>
                      <button onClick={() => deleteTemplate(tpl.id)} style={{ padding: '4px 6px', backgroundColor: '#ef4444', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '12px' }}>삭제</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* ===================== [★ 메뉴 4: 법적 효력 및 주민등록번호 수집 지침 대통합 안내] ===================== */}
        {currentMenu === 'legal' && (
          <div style={{ backgroundColor: '#fff', padding: '30px', borderRadius: '12px', border: '1px solid #e2e8f0', color: '#1e293b', lineHeight: '1.7' }}>
            <h3 style={{ margin: '0 0 10px 0', fontSize: '18px', fontWeight: 'bold', color: '#0284c7', borderBottom: '2px solid #e2e8f0', paddingBottom: '10px' }}>⚖️ 전자계약 시스템 법적 효력 및 신뢰성 지침 안내</h3>
            
            {/* ★ 에디터 화면에서 요청에 따라 이동 및 추가 완공된 고지문 가이드라인 컴포넌트 프리뷰 */}
            <div style={{ 
              background: '#f8fafc', 
              border: '1px solid #cbd5e1', 
              borderRadius: '8px', 
              padding: '18px', 
              fontSize: '13px', 
              color: '#334155', 
              lineHeight: '1.65',
              marginBottom: '25px',
              textAlign: 'left'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '10px' }}>
                <span style={{ fontSize: '15px' }}>⚖️</span>
                <strong style={{ color: '#0284c7', fontSize: '13.5px' }}>
                  주민등록번호 수집에 대한 법적 근거 및 개인정보 보호 안내 (SaaS 기본 장착 배너)
                </strong>
              </div>
              <div style={{ color: '#475569', fontSize: '12.5px' }}>
                본 단기 임대차 계약은 <strong>전자문서 및 전자거래기본법 제4조</strong> 및 <strong>전자서명법 제3조</strong>에 의거하여, 기존 종이 계약서에 서명날인한 것과 동일한 강력한 사법적 효력과 처분문서로서의 증거력이 보장됩니다.
                <br /><br />
                <strong>1. 주민등록번호 전체(13자리) 수집의 법적 필수성</strong><br />
                임대인의 소득세법 및 부가가치세법에 따른 <span style={{ color: '#0284c7', fontWeight: 'bold' }}>'주택임대 수입금액 현황신고(임차인 명세서 기재)' 의무 준수</span>를 위해 임차인의 성명, 주소와 함께 주민등록번호 전체 입력이 철저히 요구됩니다. 이는 본 계약이 위법한 미신고 숙박업 행위가 아닌, 정당한 '주택 단기 임대차 거래'임을 과세관청에 증빙하여 당사자 간의 불필요한 세무 리스크를 원천 차단하기 위한 법적 필수 절차입니다.
                <br /><br />
                <strong>2. 개인정보 보호법 제15조에 따른 안심 보안 원칙</strong><br />
                * <strong>화면 마스킹 보호:</strong> 임차인 오용 및 정보 노출 방지를 위해, 입력 즉시 뒷자리는 <span style={{ color: '#0284c7', fontWeight: 'bold' }}>암호화 마스킹 처리(예: 880101-*******)</span>되어 본인 외에는 철저히 은닉됩니다.<br />
                * <strong>격리 저장 및 자동 파기:</strong> 수집된 식별정보는 개인정보 보호법 규정에 의거하여 강력하게 난수 암호화되어 격리 저장되며, 국세청 세무 증빙 및 법정 의무 보유 기한이 경과하는 즉시 시스템에서 복구 불가능한 형태로 <span style={{ color: '#ef4444', fontWeight: 'bold' }}>자동 영구 파기</span>됩니다.
              </div>
            </div>

            <div style={{ marginTop: '20px' }}>
              <h4 style={{ fontSize: '15px', fontWeight: 'bold', color: '#0f172a', margin: '0 0 8px 0' }}>1. 모바일 전자계약의 강력한 법적 효력 및 판례 근거</h4>
              <ul style={{ paddingLeft: '20px', margin: '0 0 20px 0', fontSize: '13.5px' }}>
                <li><strong>전자문서 및 전자거래 기본법 제4조 제1항:</strong> 전자문서는 전자적 형태로 되어 있다는 이유만으로 문서로서의 효력이 부인되지 아니하며 종이 계약서와 완벽히 동일한 민사상 법적 처분 문서의 효력을 갖습니다.</li>
                <li><strong>전자서명법 제3조 제1항:</strong> 전자서명은 전자적 형태로 되어 있다는 이유만으로 서명날인으로서의 효력이 부인되지 아니하므로, 임차인이 터치 모바일 기기를 통해 입력한 전자 수기 서명은 실물 인감도장과 법적으로 완전히 동등한 자격을 지닙니다.</li>
                <li><strong>법원 주요 판례 (춘천지방법원 원주지원 선고):</strong> 비대면 모바일 메신저 링크 인증 및 터치스크린 서명 방식을 활용해 체결된 명도 약정 및 특약 계약에 대해, 법원은 "당사자 본인의 고유 식별 정보 인증 절차를 거친 전자서명은 전자서명법에 의거 날인과 동일한 성립의 진정이 인정되므로 계약의 효력은 유효하다"고 판결하여 강력한 사법적 증거력을 명시했습니다.</li>
              </ul>

              <h4 style={{ fontSize: '15px', fontWeight: 'bold', color: '#0f172a', margin: '0 0 8px 0' }}>2. 적법한 고유식별정보 수집 및 안전 표준 프로세스</h4>
              <ul style={{ paddingLeft: '20px', margin: '0 0 20px 0', fontSize: '13.5px' }}>
                <li><strong>개인정보 보호법 제15조 및 법령상 의무 이행:</strong> 국세청 주택임대 소득 신고 및 부가가치세법상 증빙 제출 의무를 준수하기 위해 거래 당사자의 고유식별 정보 기재가 필수적입니다. 본 시스템은 이를 적법하게 수집·처리합니다.</li>
                <li><strong>임차인 친화적 마스킹 기술 및 보안 파기:</strong> 계약 당사자가 정보를 열람할 때 식별번호 뒷자리는 자동 은닉(마스킹) 처리되어 정보 노출에 대한 거부감을 원천 해소합니다. 계약 이력에 바인딩되는 모든 데이터는 난수화되어 암호화 저장소에 격리되며, 세무 및 법적 보유 기한 만료 시 자동 파기됩니다.</li>
              </ul>
            </div>
          </div>
        )}

      </div>
      {/* 하단 버전 표시 */}
      <div style={{ textAlign: 'center', padding: '15px', color: '#94a3b8', fontSize: '12px', fontWeight: 'bold' }}>
        ver.260622_005
        {/* 🔐 비밀번호 변경 모달 팝업 */}
        {showPasswordModal && (
          <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', zIndex: 9999, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <div style={{ backgroundColor: '#fff', padding: '30px', borderRadius: '12px', width: '340px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
              <h3 style={{ margin: '0 0 20px 0', fontSize: '18px', color: '#1e293b', textAlign: 'center' }}>🔒 최고 관리자 비밀번호 변경</h3>
              <form onSubmit={handleChangePassword}>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '12px', color: '#64748b', marginBottom: '5px', fontWeight: 'bold' }}>현재 비밀번호</label>
                  <input type="password" value={pwChangeInput.current} onChange={(e) => setPwChangeInput({ ...pwChangeInput, current: e.target.value })} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '12px', color: '#64748b', marginBottom: '5px', fontWeight: 'bold' }}>새 비밀번호</label>
                  <input type="password" value={pwChangeInput.new} onChange={(e) => setPwChangeInput({ ...pwChangeInput, new: e.target.value })} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '25px' }}>
                  <label style={{ display: 'block', fontSize: '12px', color: '#64748b', marginBottom: '5px', fontWeight: 'bold' }}>새 비밀번호 확인</label>
                  <input type="password" value={pwChangeInput.confirm} onChange={(e) => setPwChangeInput({ ...pwChangeInput, confirm: e.target.value })} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ display: 'flex', gap: '10px' }}>
                  <button type="button" onClick={() => setShowPasswordModal(false)} style={{ flex: 1, padding: '10px', backgroundColor: '#e2e8f0', color: '#475569', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>취소</button>
                  <button type="submit" style={{ flex: 1, padding: '10px', backgroundColor: '#0284c7', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>변경 적용</button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* 보안 질문 변경 모달 */}
        {showSecuritySettingsModal && (
          <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
            <div style={{ backgroundColor: '#fff', padding: '30px', borderRadius: '12px', width: '380px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
              <h3 style={{ margin: '0 0 15px 0', fontSize: '18px', color: '#0f172a' }}>🛡️ 보안 질문/답변 설정</h3>
              <p style={{ fontSize: '12px', color: '#64748b', marginBottom: '20px', lineHeight: '1.5' }}>
                비밀번호를 분실했을 때 초기화할 수 있는 안전 장치입니다. 본인만 알 수 있는 직관적인 질문과 단답형 답변을 설정하세요.
              </p>
              <form onSubmit={handleUpdateSecuritySettings}>
                <div style={{ marginBottom: '15px' }}>
                  <input type="password" placeholder="현재 계정 비밀번호" value={securitySettingsInput.currentPassword} onChange={(e) => setSecuritySettingsInput({...securitySettingsInput, currentPassword: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 'bold', color: '#475569', marginBottom: '5px' }}>나만의 보안 질문 설정</label>
                  <input type="text" placeholder="예: 내가 가장 좋아하는 여행지는?" value={securitySettingsInput.question} onChange={(e) => setSecuritySettingsInput({...securitySettingsInput, question: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ marginBottom: '25px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 'bold', color: '#475569', marginBottom: '5px' }}>보안 답변 (띄어쓰기 무시됨)</label>
                  <input type="text" placeholder="예: 제주도" value={securitySettingsInput.answer} onChange={(e) => setSecuritySettingsInput({...securitySettingsInput, answer: e.target.value})} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box' }} required />
                </div>
                <div style={{ display: 'flex', gap: '10px' }}>
                  <button type="button" onClick={() => setShowSecuritySettingsModal(false)} style={{ flex: 1, padding: '10px', backgroundColor: '#f1f5f9', color: '#475569', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>취소</button>
                  <button type="submit" style={{ flex: 1, padding: '10px', backgroundColor: '#10b981', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>질문/답변 저장</button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
```

### `src/app/api/contract/route.ts`
```typescript
import { NextResponse } from 'next/server';
import { supabaseServer as supabase } from '@/lib/supabase-server';
import { cookies } from 'next/headers';

export async function POST(request: Request) {
  try {
    const cookieStore = await cookies();
    const sessionCookie = cookieStore.get('admin-session');
    if (!sessionCookie || sessionCookie.value !== 'authenticated') {
      return NextResponse.json({ success: false, message: '인증되지 않은 사용자입니다.' }, { status: 401 });
    }

    const body = await request.json();
    const { acc_name, room_name, start_date, end_date, deposit, price, special_terms } = body;

    if (!acc_name || !room_name) {
      return NextResponse.json({ success: false, message: '숙소명과 객실명은 필수입니다.' }, { status: 400 });
    }

    // 1. 혼동하기 쉬운 문자(I, O, 0, 1)를 제외한 고유 토큰 12자리 생성 (강력한 보안)
    const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    let contract_token = '';
    for (let i = 0; i < 12; i++) {
      contract_token += chars.charAt(Math.floor(Math.random() * chars.length));
    }

    // 1.5. 계약서 고유번호(contract_serial) 발급 로직 (한국시간 KST 기준)
    const kstDate = new Date(new Date().getTime() + 9 * 60 * 60 * 1000);
    const yy = String(kstDate.getUTCFullYear()).slice(-2);
    const mm = String(kstDate.getUTCMonth() + 1).padStart(2, '0');
    const dd = String(kstDate.getUTCDate()).padStart(2, '0');
    const datePrefix = yy + mm + dd; // 예: "260620"

    // 오늘(KST 기준) 00시 정각의 UTC 시간 계산
    const kstStartOfDayUTC = new Date(Date.UTC(kstDate.getUTCFullYear(), kstDate.getUTCMonth(), kstDate.getUTCDate(), -9, 0, 0)).toISOString();

    const { count } = await supabase
      .from('contracts')
      .select('*', { count: 'exact', head: true })
      .gte('created_at', kstStartOfDayUTC);

    const seq = ((count || 0) + 1).toString().padStart(3, '0');
    const contract_serial = `No.${datePrefix}${seq}`;

    // special_terms에 contract_serial 주입
    let parsedTerms: any = {};
    try {
      parsedTerms = JSON.parse(special_terms);
    } catch (e) {
      parsedTerms = {};
    }
    parsedTerms.contract_serial = contract_serial;

    // 🛡️ 임차인 주민번호가 관리자 작성 시 비어있다면, 템플릿의 과거 잔재가 딸려오지 않도록 완전히 초기화
    if (!parsedTerms.tenant_birthday) {
      parsedTerms.tenant_birthday = '';
      parsedTerms.tenant_birthday_full = '';
    }

    const updatedSpecialTerms = JSON.stringify(parsedTerms);

    // 2. 슈파베이스 DB 테이블에 임대인이 세팅한 정보 인서트(Insert)
    const { error } = await supabase
      .from('contracts')
      .insert([
        {
          contract_token,
          accommodation_name: acc_name,
          room_name: room_name,
          check_in_date: start_date,
          check_out_date: end_date,
          deposit_amount: deposit,
          total_amount: price,
          special_terms: updatedSpecialTerms,
          status: 'WAITING'
        }
      ]);

    if (error) throw error;

    // 3. 임차인에게 전달할 최종 싸인용 웹 페이지 고유 주소 반환
    const contract_url = `/sign/${contract_token}`;

    return NextResponse.json({ success: true, contract_url });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: '서버 오류: ' + error.message }, { status: 500 });
  }
}

```

### `src/app/sign/[token]/page.tsx`
```typescript
'use client';

import { useEffect, useState, useRef } from 'react';
import { useParams } from 'next/navigation';
import { supabase } from '@/lib/supabase';
import html2canvas from 'html2canvas';

export default function TenantSignPage() {
  const params = useParams();
  const token = params?.token as string;

  const [contract, setContract] = useState<any>(null);
  const [contractData, setContractData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  // 인적사항 입력 상태 관리
  const [tenantInput, setTenantInput] = useState({
    tenant_name: '',
    tenant_phone: '',
    tenant_birthday: '', 
    tenant_address: '',
  });

  const [isSigned, setIsSigned] = useState(false);
  const [showDesktopPreview, setShowDesktopPreview] = useState(false);
  
  // ✍️ 팝업 서명 패드 제어 상태 및 Canvas 참조
  const [showSignPopup, setShowSignPopup] = useState(false);
  const [signatureImage, setSignatureDataUrl] = useState(''); 
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const isDrawingRef = useRef(false);

  // 모바일 확대/축소(Pinch-zoom) 시 화면 정중앙을 추적하기 위한 위치 상태
  const [modalPosition, setModalPosition] = useState<{top: string|number, left: string|number, position: any, transform: string}>({
    top: '50%', left: '50%', position: 'fixed', transform: 'translate(-50%, -50%)'
  });

  useEffect(() => {
    if (showSignPopup && window.visualViewport) {
      const updatePosition = () => {
        const vv = window.visualViewport;
        if (vv) {
          setModalPosition({
            position: 'absolute',
            top: `${vv.pageTop + vv.height / 2}px`,
            left: `${vv.pageLeft + vv.width / 2}px`,
            transform: 'translate(-50%, -50%)'
          });
        }
      };
      updatePosition();
      window.visualViewport.addEventListener('resize', updatePosition);
      window.visualViewport.addEventListener('scroll', updatePosition);
      return () => {
        window.visualViewport?.removeEventListener('resize', updatePosition);
        window.visualViewport?.removeEventListener('scroll', updatePosition);
      };
    } else {
      setModalPosition({ top: '50%', left: '50%', position: 'fixed', transform: 'translate(-50%, -50%)' });
    }
  }, [showSignPopup]);

  // 📱 모바일 브라우저 확대/축소(Pinch-zoom) 활성화 및 메타태그 동적 주입
  useEffect(() => {
    const meta = document.createElement('meta');
    meta.name = 'viewport';
    // user-scalable=yes 구조를 선언하여 모바일에서 두 손가락으로 자유롭게 확대/축소가 가능합니다.
    meta.content = 'width=840, initial-scale=0.4, minimum-scale=0.1, maximum-scale=3.0, user-scalable=yes';
    document.getElementsByTagName('head')[0].appendChild(meta);

    return () => {
      document.getElementsByTagName('head')[0].removeChild(meta);
    };
  }, []);

  useEffect(() => {
    if (token) {
      fetchContractData();
    }
  }, [token]);

  const fetchContractData = async () => {
    try {
      const res = await fetch('/api/contract/get', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token })
      });
      const json = await res.json();
      if (!json.success) throw new Error(json.message);
      const data = json.data;

      if (data) {
        setContract(data);
        if (data.status === 'SIGNED') {
          setIsSigned(true);
        }
        if (data.signature_image_url) {
          setSignatureDataUrl(data.signature_image_url);
        }
        let parsed;
        try {
          parsed = typeof data.special_terms === 'string' ? JSON.parse(data.special_terms) : data.special_terms;
          setContractData(parsed);
          
          const initialBirth = (parsed.tenant_birthday_full || data.tenant_birthday || parsed.tenant_birthday || '').replace(/[^0-9]/g, '');
          setTenantInput({
            tenant_name: data.tenant_name || parsed.tenant_name || '',
            tenant_phone: data.tenant_phone || parsed.tenant_phone || '',
            tenant_birthday: initialBirth.substring(0, 13),
            tenant_address: data.tenant_address || parsed.tenant_address || '',
          });
        } catch (e) {
          setContractData(parsed || data);
        }
      }
    } catch (err) {
      console.error(err);
      alert('계약서 데이터를 불러오는 중 오류가 발생했거나 존재하지 않는 링크입니다.');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setTenantInput((prev) => ({ ...prev, [name]: value }));
  };

  // 🔒 주민등록번호 입력 핸들러 (붙여넣기 및 삭제 완벽 대응)
  const handleBirthdayChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    
    // 만약 다 지웠을 경우
    if (value === '') {
      setTenantInput((prev) => ({ ...prev, tenant_birthday: '' }));
      return;
    }

    // 화면 표시값
    const currentDisplay = getDisplayBirthday(tenantInput.tenant_birthday);

    // 지우기 처리 (백스페이스 등)
    if (value.length < currentDisplay.length) {
      setTenantInput((prev) => ({ ...prev, tenant_birthday: prev.tenant_birthday.slice(0, -1) }));
      return;
    }

    // 붙여넣기 또는 끝에 텍스트 추가 처리
    if (value.length > currentDisplay.length) {
      // 기존에 표시되던 부분을 제외하고 새로 추가된 부분만 추출
      const addedPart = value.slice(currentDisplay.length);
      const addedDigits = addedPart.replace(/[^0-9]/g, '');
      
      // 기존 입력값 끝에 새로 들어온 숫자만 이어붙이고 13자리로 제한
      if (addedDigits) {
        setTenantInput((prev) => ({
          ...prev,
          tenant_birthday: (prev.tenant_birthday + addedDigits).substring(0, 13)
        }));
      }
    }
  };

  // 👁️ 마스킹 포맷팅 함수
  const getDisplayBirthday = (raw: string) => {
    if (!raw) return '';
    if (raw.length <= 6) return raw;
    
    const front = raw.substring(0, 6);
    const gender = raw.charAt(6);
    const maskedLength = raw.length - 7;
    const stars = '*'.repeat(maskedLength > 0 ? maskedLength : 0);
    
    return front + '-' + gender + stars;
  };

  // 🎨 Canvas 드로잉 이벤트 제어 핸들러 (모바일 터치 튕김 방지 패치 포함)
  const startDrawing = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    // 팝업 패드 안에서 서명할 때 화면 전체가 스크롤되거나 움직이는 현상 방지
    if (e.cancelable) e.preventDefault();
    isDrawingRef.current = true;
    draw(e);
  };

  const stopDrawing = () => {
    isDrawingRef.current = false;
    if (canvasRef.current) {
      const ctx = canvasRef.current.getContext('2d');
      if (ctx) ctx.beginPath();
    }
  };

  const draw = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    if (!isDrawingRef.current || !canvasRef.current) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.lineWidth = 3;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#0284c7';

    const rect = canvas.getBoundingClientRect();
    let clientX = 0;
    let clientY = 0;

    if ('touches' in e) {
      if (e.touches.length === 0) return;
      clientX = e.touches[0].clientX;
      clientY = e.touches[0].clientY;
    } else {
      clientX = e.clientX;
      clientY = e.clientY;
    }

    const x = clientX - rect.left;
    const y = clientY - rect.top;

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const clearCanvas = () => {
    if (!canvasRef.current) return;
    const ctx = canvasRef.current.getContext('2d');
    if (ctx) {
      ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
      ctx.beginPath();
    }
  };

  const saveSignatureFromPopup = () => {
    if (!canvasRef.current) return;
    const dataUrl = canvasRef.current.toDataURL();
    setSignatureDataUrl(dataUrl);
    setShowSignPopup(false);
  };

  const handleDownloadImage = async () => {
    const container = document.querySelector('.print-container') as HTMLElement;
    if (!container) return;
    try {
      const canvas = await html2canvas(container, {
        scale: 2,
        useCORS: true,
        ignoreElements: (element) => element.classList.contains('no-print')
      });
      const imgData = canvas.toDataURL('image/jpeg', 0.9);
      
      const terms = contractData || {};
      const yy = terms.start_year ? terms.start_year.toString().slice(-2) : '26';
      const inDate = (terms.start_month || '') + (terms.start_day || '');
      const outDate = (terms.end_month || '') + (terms.end_day || '');
      
      let room = contract?.room_name || terms.rent_part || '';
      if (room === '독채전체' && contract?.accommodation_name) {
        const match = contract.accommodation_name.match(/(\d+)호/);
        if (match) room = match[1] + '호';
      }
      const tName = tenantInput.tenant_name || terms.tenant_name || '이름없음';
      
      const fileName = `${yy}-${inDate}-${outDate}-${room}-${tName}.jpg`.replace(/\s+/g, '');
      
      const link = document.createElement('a');
      link.href = imgData;
      link.download = fileName;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (e) {
      console.error(e);
      alert('이미지 저장 중 오류가 발생했습니다.');
    }
  };

  const handleSignSubmit = async () => {
    if (!tenantInput.tenant_address.trim()) return alert('임차인 주소를 기재해 주세요.');
    if (!tenantInput.tenant_birthday || tenantInput.tenant_birthday.length !== 13) {
      return alert('주민등록번호 13자리(생년월일 6자리 + 뒷자리 7자리)를 모두 정확히 입력해 주세요.\n(생년월일 8자리 입력 불가)');
    }
    if (!tenantInput.tenant_name.trim()) return alert('임차인 성명을 기재해 주세요.');
    if (!tenantInput.tenant_phone.trim()) return alert('임차인 연락처를 기재해 주세요.');
    if (!signatureImage) return alert('서명란을 클릭하여 친필 수기 전자서명을 완료해 주세요.');

    if (!window.confirm('입력하신 명세 정보와 서명날인 데이터로 법적 계약 체결을 완료하시겠습니까?')) return;

    setSubmitting(true);
    try {
      const safeBirthday = tenantInput.tenant_birthday;
      const newTerms = { ...contractData, tenant_birthday_full: safeBirthday };
      const res = await fetch('/api/contract/sign', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          token,
          updateData: {
            tenant_name: tenantInput.tenant_name,
            tenant_phone: tenantInput.tenant_phone,
            tenant_birthday: safeBirthday.substring(0, 6),
            tenant_address: tenantInput.tenant_address,
            status: 'SIGNED',
            signed_at: new Date().toISOString(),
            signature_image_url: signatureImage,
            special_terms: JSON.stringify(newTerms)
          }
        })
      });
      const json = await res.json();
      if (!json.success) throw new Error(json.message);

      setIsSigned(true);
      alert('✍️ 전자서명 날인이 성공적으로 마감되었습니다!');
      
      // 서명 완료 직후 시스템에서 실물계약 이미지를 자동 저장(다운로드)
      setTimeout(() => {
        handleDownloadImage();
      }, 500);
    } catch (err: any) {
      console.error(err);
      alert(`서명 보관 처리 중 장애가 발생했습니다.\n오류 원인: ${err?.message || err}`);
    } finally {
      setSubmitting(false);
    }
  };

  const triggerPrint = () => {
    window.print();
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', backgroundColor: '#f8fafc' }}>
        <p style={{ fontSize: '14px', color: '#64748b', fontWeight: 'bold' }}>📄 전자계약서 로딩 중...</p>
      </div>
    );
  }

  if (!contract || !contractData) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', backgroundColor: '#f8fafc' }}>
        <p style={{ fontSize: '14px', color: '#ef4444', fontWeight: 'bold' }}>⚠️ 유효하지 않거나 접근 권한이 없는 계약 링크입니다.</p>
      </div>
    );
  }

  return (
    <div style={{ backgroundColor: '#f0f4f8', minHeight: '100vh', padding: '20px 15px', fontFamily: 'sans-serif' }}>
      
      {/* 상단 유틸 바 컨트롤 */}
      <div style={{ maxWidth: '800px', margin: '0 auto 15px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', backgroundColor: '#fff', padding: '12px 20px', borderRadius: '8px', boxShadow: '0 2px 8px rgba(0,0,0,0.04)' }} className="no-print">
        <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#1e293b' }}>📄 임차인 확인 및 전자서명 패널</span>
        <div style={{ display: 'flex', gap: '8px' }}>
          <button onClick={triggerPrint} style={{ backgroundColor: '#475569', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer' }} className="hidden md:block">계약서 인쇄</button>
          {isSigned ? (
            <button onClick={handleDownloadImage} style={{ backgroundColor: '#15803d', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer' }} className="hidden md:block">완료된 계약서 이미지 다운로드</button>
          ) : (
            <button onClick={handleSignSubmit} disabled={isSigned || submitting} style={{ backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer' }} className="hidden md:block">실물 계약 확정/저장</button>
          )}
        </div>
      </div>

      {/* 모바일 최적화 입력 폼 (모바일에서만 표시됨, 데스크탑 미리보기 시 숨김) */}
      <div className={`no-print ${showDesktopPreview ? 'hidden' : 'block md:hidden'}`} style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '12px', boxShadow: '0 4px 15px rgba(0,0,0,0.06)' }}>
        <div style={{ background: '#f0fdf4', border: '1px solid #bbf7d0', borderRadius: '8px', padding: '15px', marginBottom: '20px', fontSize: '13px', color: '#166534' }}>
          <strong style={{ fontSize: '14px' }}>📱 모바일 간편 서명</strong><br/>
          계약에 필요한 아래 정보를 입력하시고 서명을 완료해주세요.
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>성명</label>
          <input type="text" name="tenant_name" value={tenantInput.tenant_name} onChange={handleInputChange} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', marginTop: '5px', backgroundColor: isSigned ? '#f1f5f9' : 'yellow' }} placeholder="임차인 성명" disabled={isSigned} />
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>주민등록번호 13자리</label>
          <input type="text" value={getDisplayBirthday(tenantInput.tenant_birthday)} onChange={handleBirthdayChange} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', marginTop: '5px', backgroundColor: isSigned ? '#f1f5f9' : 'yellow' }} placeholder="앞 6자리 + 뒤 7자리 모두 입력" disabled={isSigned} />
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>연락처</label>
          <input type="text" name="tenant_phone" value={tenantInput.tenant_phone} onChange={handleInputChange} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', marginTop: '5px', backgroundColor: isSigned ? '#f1f5f9' : 'yellow' }} placeholder="010-0000-0000" disabled={isSigned} />
        </div>

        <div style={{ marginBottom: '20px' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>주민등록상 주소지</label>
          <input type="text" name="tenant_address" value={tenantInput.tenant_address} onChange={handleInputChange} style={{ width: '100%', padding: '10px', border: '1px solid #cbd5e1', borderRadius: '6px', marginTop: '5px', backgroundColor: isSigned ? '#f1f5f9' : 'yellow' }} placeholder="주민등록상 주소지를 입력하세요" disabled={isSigned} />
        </div>

        <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f8fafc', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '10px' }}>전자 서명</label>
          {signatureImage ? (
            <img src={signatureImage} alt="임차인 수기서명" style={{ height: '50px', border: '1px solid #e2e8f0', backgroundColor: '#fff', cursor: isSigned ? 'default' : 'pointer' }} onClick={() => !isSigned && setShowSignPopup(true)} />
          ) : isSigned ? (
            <span style={{ fontSize: '14px', fontWeight: 'bold', color: '#15803d' }}>서명 완료됨</span>
          ) : (
            <button type="button" onClick={() => setShowSignPopup(true)} style={{ width: '100%', padding: '12px', backgroundColor: 'yellow', border: '1px dashed #0284c7', color: '#0284c7', borderRadius: '6px', fontWeight: 'bold' }}>👉 서명 패드 열기</button>
          )}
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <button onClick={() => setShowDesktopPreview(true)} style={{ padding: '14px', backgroundColor: '#f1f5f9', color: '#475569', borderRadius: '8px', fontWeight: 'bold', border: 'none' }}>📄 실물 계약서 원본 전체보기</button>
          {!isSigned && (
            <button onClick={handleSignSubmit} disabled={submitting} style={{ padding: '14px', backgroundColor: '#0284c7', color: '#fff', borderRadius: '8px', fontWeight: 'bold', border: 'none' }}>{submitting ? '처리 중...' : '📝 계약서 확정 및 제출하기'}</button>
          )}
        </div>
      </div>

      {/* 데스크탑 뷰 및 모바일 원본보기 (가로 스크롤 가능하도록 감싸기) */}
      <div className={`print-block ${showDesktopPreview ? 'block' : 'hidden md:block'}`} style={{ width: '100%', overflowX: 'auto', paddingBottom: '20px' }}>
        {showDesktopPreview && (
          <button onClick={() => setShowDesktopPreview(false)} className="no-print" style={{ marginBottom: '15px', padding: '10px 15px', backgroundColor: '#334155', color: '#fff', borderRadius: '6px', border: 'none', fontWeight: 'bold', display: 'block', width: '100%' }}>⬅ 모바일 입력 폼으로 돌아가기</button>
        )}
        {/* 실물 크기를 그대로 유지하도록 minWidth 설정 바인딩 */}
        <div className="print-container" style={{ maxWidth: '800px', minWidth: '800px', margin: '0 auto', backgroundColor: '#fff', color: '#000', padding: '30px 20px', borderRadius: '12px', boxShadow: '0 4px 15px rgba(0,0,0,0.06)', border: '1px solid #e2e8f0', boxSizing: 'border-box' }}>
        
        {/* 최상단 법적 고지 배너 */}
        <div className="no-print" style={{ background: '#f0fdf4', border: '1px solid #bbf7d0', borderRadius: '8px', padding: '18px', marginBottom: '25px', fontSize: '13px', color: '#166534', lineHeight: '1.65', textAlign: 'left' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
            <span style={{ fontSize: '15px' }}>⚖️</span>
            <strong style={{ color: '#15803d', fontSize: '14px' }}>주민등록번호 수집 법적 근거 및 개인정보 암호화 고지</strong>
          </div>
          <div style={{ color: '#166534', fontSize: '12.5px' }}>
            본 계약은 <strong>전자문서 및 전자거래기본법 제4조</strong> 및 <strong>전자서명법 제3조</strong>에 의거하여 종이 계약과 동일한 법적 효력을 가집니다. 임대차 계약서 작성 및 확정일자 신청, 국세청 신고 등 부동산 거래의 이행을 위해 <strong>부동산 거래신고 등에 관한 법률 및 공인중개사법</strong>에 의거하여 계약 당사자의 주민등록번호 전체 자리를 고지 및 필수 수집합니다. 
            <br /><br />
            입력하신 고유식별정보는 수집 즉시 최고 수준의 <strong>양방향 암호화 처리</strong>를 거쳐 데이터베이스에 안전하게 격리 보관되며, 계약 목적 외에 절대 열람되거나 활용되지 않습니다. 계약 기간 만료 및 법정 보존 의무 기간이 경과한 후에는 안전하게 영구 폐기되오니 임차인께서는 안심하고 작성하셔도 좋습니다.
          </div>
        </div>

        {isSigned && (
          <div className="no-print" style={{ backgroundColor: '#dcfce7', border: '1px solid #22c55e', color: '#15803d', padding: '15px', borderRadius: '8px', textAlign: 'center', fontWeight: 'bold', marginBottom: '25px', fontSize: '14px' }}>
            ✓ 전자 서명 합의 절차가 완료된 체결 문서입니다.
          </div>
        )}

        {/* 실물 종이 형태 서식 영역 */}
        <div style={{ border: '1px solid #000', padding: '25px 20px', position: 'relative' }}>
          {contractData.contract_serial && (
            <div style={{ position: 'absolute', top: '20px', right: '20px', fontSize: '11px', color: '#475569', fontFamily: 'monospace' }}>
              {contractData.contract_serial}
            </div>
          )}
          <h2 style={{ textAlign: 'center', fontSize: '22px', fontWeight: 'bold', margin: '0 0 5px 0', letterSpacing: '2px' }}>{contractData.main_title || '단기 임대차 계약서'}</h2>
          <p style={{ textAlign: 'center', fontSize: '11px', color: '#475569', margin: '0 0 25px 0' }}>{contractData.main_description}</p>

          <h4 style={{ fontSize: '12.5px', margin: '0 0 6px 0', fontWeight: 'bold' }}>{contractData.title_article_1 || '[제1조] 부동산의 표시'}</h4>
          <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '15px', fontSize: '11.5px' }}>
            <tbody>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '80px', textAlign: 'center' }}>{contractData.lbl_address || '주 소'}</td>
                <td colSpan={5} style={{ border: '1px solid #000', padding: '6px' }}>{contractData.address_main}</td>
              </tr>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}>{contractData.lbl_rent_part || '임대부분'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.rent_part}</td>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '70px', textAlign: 'center' }}>{contractData.lbl_house_type || '주택유형'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.house_type}</td>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '50px', textAlign: 'center' }}>{contractData.lbl_area || '면 적'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.area_size}</td>
              </tr>
            </tbody>
          </table>

          <h4 style={{ fontSize: '12.5px', margin: '15px 0 6px 0', fontWeight: 'bold' }}>{contractData.title_article_2 || '[제2조] 계약조건'}</h4>
          <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '15px', fontSize: '11.5px' }}>
            <tbody>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '80px', textAlign: 'center' }}>{contractData.lbl_period || '사용기간'}</td>
                <td colSpan={3} style={{ border: '1px solid #000', padding: '6px' }}>
                  {contractData.start_year}년 {contractData.start_month}월 {contractData.start_day}일 부터 ~ {contractData.end_year}년 {contractData.end_month}월 {contractData.end_day}일 까지
                </td>
              </tr>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}>{contractData.lbl_deposit || '보증금'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.deposit}</td>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '80px', textAlign: 'center' }}>{contractData.lbl_premium || '관리비'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.premium}</td>
              </tr>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}>{contractData.lbl_price || '이용금액'}</td>
                <td style={{ border: '1px solid #000', padding: '6px', fontWeight: 'bold' }}>{contractData.total_amount}</td>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}>{contractData.lbl_cleaning || '청소비'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>{contractData.cleaning_fee}</td>
              </tr>
            </tbody>
          </table>

          <h4 style={{ fontSize: '12.5px', margin: '15px 0 6px 0', fontWeight: 'bold' }}>{contractData.title_article_3 || '[제3조] 대금 지급방식'}</h4>
          <table style={{ width: '100%', borderCollapse: 'collapse', marginBottom: '15px', fontSize: '11.5px' }}>
            <tbody>
              <tr>
                <td style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '80px', textAlign: 'center' }}>{contractData.lbl_total || '총액'}</td>
                <td style={{ border: '1px solid #000', padding: '6px' }}>
                  {contractData.pay_amount} ({contractData.pay_year}년 {contractData.pay_month}월 {contractData.pay_day}일 {contractData.lbl_pay_status})
                </td>
              </tr>
            </tbody>
          </table>

          <h4 style={{ fontSize: '12.5px', margin: '15px 0 4px 0', fontWeight: 'bold' }}>{contractData.title_article_4}</h4>
          <div style={{ fontSize: '11px', whiteSpace: 'pre-wrap', lineHeight: '1.5', padding: '8px', border: '1px solid #e2e8f0', marginBottom: '10px' }}>{contractData.article_4}</div>

          <h4 style={{ fontSize: '12.5px', margin: '15px 0 4px 0', fontWeight: 'bold' }}>{contractData.title_article_5}</h4>
          <div style={{ fontSize: '11px', whiteSpace: 'pre-wrap', lineHeight: '1.5', padding: '8px', border: '1px solid #e2e8f0', marginBottom: '10px' }}>{contractData.article_5}</div>

          <h4 style={{ fontSize: '12.5px', margin: '15px 0 4px 0', fontWeight: 'bold' }}>{contractData.title_article_6 || '[제6조] 특약사항'}</h4>
          <div style={{ fontSize: '11px', whiteSpace: 'pre-wrap', lineHeight: '1.5', padding: '8px', border: '1px solid #e2e8f0', marginBottom: '20px' }}>{contractData.special_terms}</div>

          <div style={{ textAlign: 'center', fontSize: '12.5px', fontWeight: 'bold', margin: '20px 0 15px' }}>
            {contractData.contract_year}년 {contractData.contract_month}월 {contractData.contract_day}일
          </div>

          {/* 명세 연동 테이블 */}
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '11px' }}>
            <tbody>
              <tr>
                <td rowSpan={2} style={{ border: '1px solid #000', backgroundColor: '#f8fafc', fontWeight: 'bold', width: '35px', textAlign: 'center' }}>{contractData.lbl_host_title || '임대인'}</td>
                <td style={{ border: '1px solid #000', padding: '5px', backgroundColor: '#f8fafc', width: '65px', textAlign: 'center' }}>{contractData.lbl_host_addr || '주 소'}</td>
                <td style={{ border: '1px solid #000', padding: '5px' }}>{contractData.host_address}</td>
                <td style={{ border: '1px solid #000', padding: '5px', backgroundColor: '#f8fafc', width: '60px', textAlign: 'center' }}>{contractData.lbl_host_name || '상호/이름'}</td>
                <td style={{ border: '1px solid #000', padding: '5px', fontWeight: 'bold' }}>{contractData.host_name} (인)</td>
              </tr>
              <tr>
                <td style={{ border: '1px solid #000', padding: '5px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_host_biz || '등록번호'}</td>
                <td style={{ border: '1px solid #000', padding: '5px' }}>{contractData.host_business_num}</td>
                <td style={{ border: '1px solid #000', padding: '5px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_host_phone || '연락처'}</td>
                <td style={{ border: '1px solid #000', padding: '5px' }}>{contractData.host_phone}</td>
              </tr>

              {/* 임차인 입력 영역 */}
              <tr>
                <td rowSpan={2} style={{ border: '1px solid #000', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center' }}>{contractData.lbl_tenant_title || '임차인'}</td>
                <td style={{ border: '1px solid #000', padding: '4px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_tenant_addr || '주 소'}</td>
                <td style={{ border: '1px solid #000', padding: '2px' }}>
                  {isSigned ? (
                    <span style={{ paddingLeft: '6px' }}>{tenantInput.tenant_address}</span>
                  ) : (
                    <input 
                      type="text" 
                      name="tenant_address" 
                      value={tenantInput.tenant_address} 
                      onChange={handleInputChange} 
                      placeholder="주민등록상 주소지를 입력하세요." 
                      style={{ width: '98%', border: 'none', padding: '5px', fontSize: '11px', outline: 'none', backgroundColor: 'yellow' }} 
                      required 
                    />
                  )}
                </td>
                <td style={{ border: '1px solid #000', padding: '4px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_tenant_name || '성 명'}</td>
                <td style={{ border: '1px solid #000', padding: '2px' }}>
                  {isSigned ? (
                    <span style={{ paddingLeft: '6px', fontWeight: 'bold' }}>{tenantInput.tenant_name}</span>
                  ) : (
                    <input 
                      type="text" 
                      name="tenant_name" 
                      value={tenantInput.tenant_name} 
                      onChange={handleInputChange} 
                      placeholder="성명" 
                      style={{ width: '95%', border: 'none', padding: '5px', fontSize: '11px', fontWeight: 'bold', outline: 'none', backgroundColor: 'yellow' }} 
                      required 
                    />
                  )}
                </td>
              </tr>
              <tr>
                <td style={{ border: '1px solid #000', padding: '4px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_tenant_birth || '주민번호'}</td>
                <td style={{ border: '1px solid #000', padding: '2px' }}>
                  {isSigned ? (
                    <span style={{ paddingLeft: '6px', fontFamily: 'monospace' }}>
                      {tenantInput.tenant_birthday.length === 13 ? tenantInput.tenant_birthday.substring(0, 6) + '-' + tenantInput.tenant_birthday.substring(6) : tenantInput.tenant_birthday}
                    </span>
                  ) : (
                    <input 
                      type="text" 
                      value={getDisplayBirthday(tenantInput.tenant_birthday)} 
                      onChange={handleBirthdayChange} 
                      placeholder="주민번호 13자리 (앞6+뒤7) 모두 입력" 
                      style={{ width: '95%', border: 'none', padding: '5px', fontSize: '11px', fontFamily: 'monospace', letterSpacing: '1px', outline: 'none', backgroundColor: 'yellow', fontWeight: 'bold' }} 
                      required 
                    />
                  )}
                </td>
                <td style={{ border: '1px solid #000', padding: '4px', backgroundColor: '#f8fafc', textAlign: 'center' }}>{contractData.lbl_tenant_phone || '연락처'}</td>
                <td style={{ border: '1px solid #000', padding: '2px' }}>
                  {isSigned ? (
                    <span style={{ paddingLeft: '6px' }}>{tenantInput.tenant_phone}</span>
                  ) : (
                    <input 
                      type="text" 
                      name="tenant_phone" 
                      value={tenantInput.tenant_phone} 
                      onChange={handleInputChange} 
                      placeholder="010-0000-0000" 
                      style={{ width: '95%', border: 'none', padding: '5px', fontSize: '11px', outline: 'none', backgroundColor: 'yellow' }} 
                      required 
                    />
                  )}
                </td>
              </tr>

              {/* ✍️ 친필 서명 패널 */}
              <tr>
                <td style={{ border: '1px solid #000', backgroundColor: '#f8fafc', fontWeight: 'bold', textAlign: 'center', padding: '12px 0' }}>서명</td>
                <td colSpan={4} style={{ border: '1px solid #000', padding: '6px', backgroundColor: '#fff' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
                    <span style={{ fontSize: '11px', color: '#475569' }}>전자서명 날인:</span>
                    {signatureImage ? (
                      <img src={signatureImage} alt="임차인 수기서명" style={{ height: '45px', border: '1px solid #e2e8f0', backgroundColor: '#f8fafc', cursor: isSigned ? 'default' : 'pointer' }} onClick={() => !isSigned && setShowSignPopup(true)} />
                    ) : isSigned ? (
                      <span style={{ fontSize: '12px', fontWeight: 'bold', color: '#15803d' }}>서명 완료됨</span>
                    ) : (
                      <button type="button" onClick={() => setShowSignPopup(true)} style={{ backgroundColor: 'yellow', border: '1px dashed #0284c7', color: '#0284c7', padding: '6px 14px', borderRadius: '4px', fontSize: '11.5px', fontWeight: 'bold', cursor: 'pointer' }}>
                        👉 여기를 클릭하여 팝업 서명패드 열기
                      </button>
                    )}
                    {!isSigned && signatureImage && (
                      <button type="button" onClick={() => setShowSignPopup(true)} style={{ fontSize: '10.5px', color: '#64748b', background: 'none', border: 'none', cursor: 'pointer', textDecoration: 'underline' }}>서명 재작성</button>
                    )}
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        {/* 최종 전송 완료 버튼 */}
        {!isSigned && (
          <div style={{ marginTop: '20px' }} className="no-print hidden md:block">
            <button type="button" onClick={handleSignSubmit} disabled={submitting} style={{ width: '100%', backgroundColor: '#0284c7', color: '#fff', padding: '16px', border: 'none', borderRadius: '8px', fontSize: '15px', fontWeight: 'bold', cursor: 'pointer', boxShadow: '0 4px 6px rgba(2, 132, 199, 0.2)' }}>
              {submitting ? '🔒 계약 정보 체결 처리 중...' : '📝 위 실물 계약서 내용대로 최종 서명 완료하기'}
            </button>
          </div>
        )}

      </div>
      </div>

      {/* ===================== ✍️ 레이어 팝업 전자서명 모달 창 ===================== */}
      {showSignPopup && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(15, 23, 42, 0.6)', zIndex: 5000 }} className="no-print">
          <div style={{ position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: '#fff', padding: '20px', borderRadius: '12px', width: '90%', maxWidth: '420px', boxShadow: '0 20px 25px -5px rgba(0,0,0,0.1)', zIndex: 5001 }}>
            <h3 style={{ margin: '0 0 5px 0', fontSize: '14px', fontWeight: 'bold', color: '#1e293b', textAlign: 'center' }}>✍️ 모도 친필 수기 서명 패드</h3>
            <p style={{ textAlign: 'center', fontSize: '11px', color: '#64748b', margin: '0 0 15px 0' }}>네모 박스 안에 직접 손가락이나 마우스로 사인을 그려주세요.</p>
            
            <div style={{ border: '2px solid #cbd5e1', borderRadius: '6px', overflow: 'hidden', backgroundColor: '#f8fafc' }}>
              <canvas 
                ref={canvasRef}
                width={380}
                height={200}
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
                onTouchStart={startDrawing}
                onTouchMove={draw}
                onTouchEnd={stopDrawing}
                style={{ display: 'block', cursor: 'crosshair', touchAction: 'none' }}
              />
            </div>

            <div style={{ display: 'flex', gap: '8px', marginTop: '15px' }}>
              <button type="button" onClick={clearCanvas} style={{ flex: 1, backgroundColor: '#f1f5f9', color: '#334155', border: 'none', padding: '10px', borderRadius: '6px', fontSize: '12.5px', fontWeight: 'bold', cursor: 'pointer' }}>다시 그리기</button>
              <button type="button" onClick={saveSignatureFromPopup} style={{ flex: 2, backgroundColor: '#0284c7', color: '#fff', border: 'none', padding: '10px', borderRadius: '6px', fontSize: '12.5px', fontWeight: 'bold', cursor: 'pointer' }}>서명 적용하기</button>
            </div>
            <button type="button" onClick={() => setShowSignPopup(false)} style={{ display: 'block', width: '100%', marginTop: '10px', background: 'none', border: 'none', color: '#94a3b8', fontSize: '11.5px', cursor: 'pointer', textDecoration: 'underline' }}>창 닫기</button>
          </div>
        </div>
      )}

      {/* 하단 버전 표시 */}
      <div className="no-print" style={{ textAlign: 'center', padding: '15px', color: '#94a3b8', fontSize: '11px', fontWeight: 'bold' }}>
        ver.260622_007
      </div>

      {/* 출력 인쇄 스타일 바인딩 및 Next.js N 개발 뱃지 강제 숨김 처리 */}
      <style jsx global>{`
        @media print {
          @page { margin: 8mm; }
          .no-print { display: none !important; }
          .print-block { display: block !important; }
          .print-container { border: none !important; padding: 0 !important; margin: 0 !important; box-shadow: none !important; min-width: 100% !important; }
          body { backgroundColor: #fff !important; padding: 0 !important; }
          div { box-shadow: none !important; }
          table { page-break-inside: avoid; break-inside: avoid; margin-bottom: 8px !important; }
          tr { page-break-inside: avoid; break-inside: avoid; }
          td { padding: 4px !important; }
          /* 여백을 줄여서 1페이지 안에 모두 들어가도록 강력 조정 */
          h2 { margin-bottom: 2px !important; }
          h4 { margin-top: 8px !important; margin-bottom: 2px !important; }
          p { margin-bottom: 10px !important; }
          .print-container > div { padding: 10px !important; }
        }
        /* 🚫 왼쪽 하단 Next.js 개발 표시기 배너 완벽 숨김 */
        next-route-announcer, 
        #nextjs-dev-indicator, 
        [id^="__next-deferred-"], 
        div[style*="position: fixed"][style*="bottom: 0px"][style*="left: 0px"],
        div[style*="position:fixed"][style*="bottom:0"][style*="left:0"] { 
          display: none !important; 
          visibility: hidden !important; 
          opacity: 0 !important;
          pointer-events: none !important;
        }
      `}</style>

    </div>
  );
}// trigger build 

```

### `public/robots.txt`
```txt
User-agent: *
Disallow: /
```

## 5. 배포 (Vercel)
Vercel에 배포할 때는 개인정보 보호를 위해 public/robots.txt 및 layout.tsx의 noindex 설정이 포함되어야 합니다.
Vercel 대시보드에서 환경 변수를 추가한 뒤 배포를 진행하세요.

```bash
npx vercel deploy --prod --yes
```


### `src/app/api/admin/templates/route.ts`
```typescript
import { NextResponse } from 'next/server';
import { supabaseServer as supabase } from '@/lib/supabase-server';
import { cookies } from 'next/headers';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    const cookieStore = await cookies();
    const sessionCookie = cookieStore.get('admin-session');
    if (!sessionCookie || sessionCookie.value !== 'authenticated') {
      return NextResponse.json({ success: false, message: '인증되지 않은 사용자입니다.' }, { status: 401 });
    }

    const { data, error } = await supabase
      .from('contract_templates')
      .select('*')
      .order('created_at', { ascending: true });

    if (error) throw error;

    return NextResponse.json({ success: true, templates: data || [] });
  } catch (err: any) {
    return NextResponse.json({ success: false, message: err.message }, { status: 500 });
  }
}

export async function POST(request: Request) {
  try {
    const cookieStore = await cookies();
    const sessionCookie = cookieStore.get('admin-session');
    if (!sessionCookie || sessionCookie.value !== 'authenticated') {
      return NextResponse.json({ success: false, message: '인증되지 않은 사용자입니다.' }, { status: 401 });
    }

    const body = await request.json();

    // 1. 벌크 동기화 (로컬스토리지 -> DB 일괄 저장)
    if (body.bulkTemplates && Array.isArray(body.bulkTemplates)) {
      for (const t of body.bulkTemplates) {
        if (!t.name) continue;
        const id = String(t.id || Date.now());
        await supabase.from('contract_templates').upsert({
          id,
          name: t.name,
          data: t.data,
          updated_at: new Date().toISOString()
        });
      }
      const { data } = await supabase.from('contract_templates').select('*').order('created_at', { ascending: true });
      return NextResponse.json({ success: true, templates: data || [] });
    }

    // 2. 삭제 요청 처리
    if (body.action === 'delete') {
      const { id } = body;
      if (!id) return NextResponse.json({ success: false, message: '삭제할 템플릿 ID가 필요합니다.' }, { status: 400 });
      const { error } = await supabase.from('contract_templates').delete().eq('id', String(id));
      if (error) throw error;
      return NextResponse.json({ success: true, message: '템플릿이 삭제되었습니다.' });
    }

    // 3. 단일 템플릿 저장 / 업데이트
    const { template } = body;
    if (!template || !template.name) {
      return NextResponse.json({ success: false, message: '템플릿 정보가 올바르지 않습니다.' }, { status: 400 });
    }

    const id = String(template.id || Date.now());
    const { data, error } = await supabase
      .from('contract_templates')
      .upsert({
        id,
        name: template.name.trim(),
        data: template.data,
        updated_at: new Date().toISOString()
      })
      .select()
      .single();

    if (error) throw error;

    return NextResponse.json({ success: true, template: data });
  } catch (err: any) {
    return NextResponse.json({ success: false, message: err.message }, { status: 500 });
  }
}

```


### `src/app/api/contract/get/route.ts`
```typescript
import { NextResponse } from 'next/server';
import { supabaseServer } from '@/lib/supabase-server';
import { checkRateLimit, getClientIp } from '@/lib/rate-limit';

export async function POST(request: Request) {
  try {
    // 🛡️ 1. 무차별 대입 및 스캐너 봇 차단 (IP당 1분 최대 30회)
    const clientIp = getClientIp(request);
    const rateCheck = checkRateLimit(`contract_get_${clientIp}`, 30, 60 * 1000);
    if (!rateCheck.success) {
      return NextResponse.json(
        { success: false, message: '요청 횟수를 초과했습니다. 잠시 후 다시 시도해 주세요.' },
        { status: 429 }
      );
    }

    const { token } = await request.json();
    if (!token) return NextResponse.json({ success: false, message: 'Token required' }, { status: 400 });

    // 🛡️ 2. 토큰 포맷 정밀 검증 (6~32자리 영문/숫자 외 입력 시 DB 접근 차단)
    if (typeof token !== 'string' || !/^[A-Za-z0-9]{6,32}$/.test(token.trim())) {
      return NextResponse.json({ success: false, message: '유효하지 않은 계약서 식별자입니다.' }, { status: 400 });
    }

    const { data, error } = await supabaseServer
      .from('contracts')
      .select('*')
      .eq('contract_token', token.trim())
      .single();

    if (error || !data) {
      return NextResponse.json({ success: false, message: '해당 계약서를 찾을 수 없습니다.' }, { status: 404 });
    }

    return NextResponse.json({ success: true, data });
  } catch (err: any) {
    return NextResponse.json({ success: false, message: '서버 오류 발생' }, { status: 500 });
  }
}

```


### `src/app/api/contract/sign/route.ts`
```typescript
import { NextResponse } from 'next/server';
import { supabaseServer } from '@/lib/supabase-server';
import { checkRateLimit, getClientIp } from '@/lib/rate-limit';

export async function POST(request: Request) {
  try {
    // 🛡️ 1. 서명 제출 요청 빈도 제어 (IP당 1분 최대 10회)
    const clientIp = getClientIp(request);
    const rateCheck = checkRateLimit(`contract_sign_${clientIp}`, 10, 60 * 1000);
    if (!rateCheck.success) {
      return NextResponse.json(
        { success: false, message: '요청 횟수를 초과했습니다. 잠시 후 다시 시도해 주세요.' },
        { status: 429 }
      );
    }

    const body = await request.json();
    const { token, updateData } = body;

    if (!token || typeof token !== 'string' || !/^[A-Za-z0-9]{6,32}$/.test(token.trim())) {
      return NextResponse.json({ success: false, message: '유효하지 않은 계약서 식별자입니다.' }, { status: 400 });
    }

    if (!updateData || typeof updateData !== 'object') {
      return NextResponse.json({ success: false, message: '서명 정보가 누락되었습니다.' }, { status: 400 });
    }

    // 🛡️ 2. 체결 완료 계약서 위·변조 방지 락 (이미 서명 체결된 계약서는 수정 불가)
    const { data: existingContract, error: fetchError } = await supabaseServer
      .from('contracts')
      .select('status')
      .eq('contract_token', token.trim())
      .single();

    if (fetchError || !existingContract) {
      return NextResponse.json({ success: false, message: '해당 계약서를 찾을 수 없습니다.' }, { status: 404 });
    }

    if (existingContract.status === 'SIGNED') {
      return NextResponse.json(
        { success: false, message: '이미 서명 체결이 완료된 계약서는 법적 효력 및 위·변조 방지를 위해 수정할 수 없습니다.' },
        { status: 400 }
      );
    }

    // 🛡️ 3. 화이트리스트 기반 안전 필드만 추출 (Mass Assignment 차단)
    const allowedUpdates = {
      tenant_name: updateData.tenant_name,
      tenant_phone: updateData.tenant_phone,
      tenant_birthday: updateData.tenant_birthday,
      tenant_address: updateData.tenant_address,
      status: 'SIGNED',
      signed_at: new Date().toISOString(),
      signature_image_url: updateData.signature_image_url,
      special_terms: updateData.special_terms,
      updated_at: new Date().toISOString(),
    };

    const { error } = await supabaseServer
      .from('contracts')
      .update(allowedUpdates)
      .eq('contract_token', token.trim());

    if (error) throw error;
    return NextResponse.json({ success: true, message: '서명이 안전하게 체결되었습니다.' });
  } catch (err: any) {
    return NextResponse.json({ success: false, message: '서버 오류 발생' }, { status: 500 });
  }
}

```


### `src/lib/rate-limit.ts`
```typescript
interface RateLimitRecord {
  count: number;
  resetTime: number;
}

const ipMap = new Map<string, RateLimitRecord>();

// 5분마다 만료된 캐시 정리하여 메모리 누수 방지
if (typeof setInterval !== 'undefined') {
  setInterval(() => {
    const now = Date.now();
    for (const [ip, record] of ipMap.entries()) {
      if (now > record.resetTime) {
        ipMap.delete(ip);
      }
    }
  }, 5 * 60 * 1000);
}

/**
 * IP 기반 요청 빈도 제어 (Rate Limiting)
 * @param ip 클라이언트 IP 주소
 * @param limit 윈도우 당 허용 최대 요청 수 (기본: 30회)
 * @param windowMs 시간 윈도우 (밀리초, 기본: 1분)
 */
export function checkRateLimit(ip: string, limit: number = 30, windowMs: number = 60 * 1000): { success: boolean; remaining: number } {
  const now = Date.now();
  const record = ipMap.get(ip);

  if (!record || now > record.resetTime) {
    ipMap.set(ip, { count: 1, resetTime: now + windowMs });
    return { success: true, remaining: limit - 1 };
  }

  if (record.count >= limit) {
    return { success: false, remaining: 0 };
  }

  record.count += 1;
  return { success: true, remaining: limit - record.count };
}

/**
 * 프록시/로드밸런서 환경에서 클라이언트 실제 IP 추출
 */
export function getClientIp(request: Request): string {
  const forwarded = request.headers.get('x-forwarded-for');
  if (forwarded) {
    return forwarded.split(',')[0].trim();
  }
  return request.headers.get('x-real-ip') || 'unknown';
}

```
