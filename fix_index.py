import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. extract the problems section block. 
# There are two problems blocks now due to the previous error.
# Let's just fix it by replacing the whole area between Hero Section and Pricing Section.

hero_end_marker = "                    {/* Problems Section */}"
pricing_start_marker = "                    {/* Pricing Section - Google Style */}"

before_hero = content.split(hero_end_marker)[0]
after_pricing = content.split(pricing_start_marker)[1]

portfolio_code = """                    {/* Portfolio Showcase Section (Awwwards Style) */}
                    <section id="portfolio" className="py-32 bg-slate-950 overflow-hidden">
                        <div className="max-w-7xl mx-auto px-5 mb-16 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-6" data-aos="fade-up">
                            <div>
                                <h2 className="text-4xl sm:text-6xl font-black mb-4 sm:mb-6 text-white tracking-tighter">제작 예시 및 금액</h2>
                                <p className="text-slate-400 text-lg sm:text-xl">탁월한 퀄리티로 완성된 파트너사들의 실제 웹사이트 예시입니다.</p>
                            </div>
                            <a href="portfolio.html" className="flex items-center gap-2 bg-brand-600/20 text-brand-400 hover:bg-brand-600 hover:text-white px-6 py-3 rounded-full font-black transition-all whitespace-nowrap shrink-0 text-lg sm:text-xl border border-brand-500/30">
                                전체보기 <Icon name="arrow-right" size={24} />
                            </a>
                        </div>
                        
                        {/* Rolling Marquee for Portfolio */}
                        <div className="relative group">
                            <div id="portfolio-slider" className="flex gap-8 overflow-x-auto hide-scrollbar px-5 pb-10 snap-x" style={{ scrollBehavior: 'smooth' }}>
                                {/* 더 자연스러운 롤링을 위해 2번 반복 */}
                                {[...portfolios, ...portfolios].map((item, i) => (
                                    <a key={i} href={item.url} target="_blank" rel="noreferrer" className="shrink-0 w-[350px] sm:w-[400px] snap-center group block">
                                        <div className="overflow-hidden rounded-2xl mb-5 shadow-2xl bg-slate-800 aspect-[4/3] relative border border-slate-700/50 group-hover:border-brand-500/50 transition-colors">
                                            <img src={item.img} alt={item.name} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-in-out opacity-80 group-hover:opacity-100" />
                                            <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent opacity-60"></div>
                                        </div>
                                        <div className="flex justify-between items-start">
                                            <div>
                                                <h3 className="text-2xl font-black text-slate-100 mb-1 group-hover:text-brand-400 transition-colors">{item.name}</h3>
                                                <p className="text-slate-400 text-sm font-medium">제작 비용: <span className="text-brand-400 font-bold">{item.price}</span></p>
                                            </div>
                                            <div className="w-10 h-10 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center group-hover:bg-brand-600 transition-colors text-white">
                                                <Icon name="arrow-up-right" size={18} />
                                            </div>
                                        </div>
                                    </a>
                                ))}
                            </div>
                            
                            {/* Gradient Masks */}
                            <div className="absolute top-0 bottom-0 left-0 w-24 bg-gradient-to-r from-slate-950 to-transparent pointer-events-none"></div>
                            <div className="absolute top-0 bottom-0 right-0 w-24 bg-gradient-to-l from-slate-950 to-transparent pointer-events-none"></div>
                        </div>
                    </section>
"""

problems_code = """
                    {/* Problems Section */}
                    <section id="problems" className="py-32 px-5 bg-slate-950">
                        <div className="max-w-6xl mx-auto text-center mb-20" data-aos="fade-up">
                            <h2 className="text-3xl sm:text-5xl font-black mb-8 leading-tight">사업 매출의 핵심,<br/><span className="text-brand-500">왜 온라인 홍보</span>를 포기하시나요?</h2>
                            <p className="text-slate-400 text-lg">사장님의 고민, 효율적인 구조로 해결해드립니다.</p>
							<p className="text-slate-400 text-lg">홈페이지 제작 10만원, 월 1만원으로 검색엔진 등록과 홍보까지~</p>
                        </div>
                        <div className="max-w-6xl mx-auto grid sm:grid-cols-2 gap-8">
                            {[
                                {icon:'clock', title:'시간 부족', desc:'바쁜 사장님을 위해, 제작과 홍보 마케팅을 대신합니다.'},
                                {icon:'dollar-sign', title:'비싼 비용', desc:'홈페이지 제작과 홍보 비용의 거품을 걷어냈습니다.'},
                                {icon:'monitor', title:'정보 부족', desc:'포털 등록 등 어디서부터 손대야 할지 막막한 환경을 정리합니다.'},
                                {icon:'search', title:'검색 등록', desc:'훌륭한 사업장이 포털 지도 노출 되게 설정해 드립니.'},
                                {icon:'message-circle', title:'사후 관리', desc:'제작 후 끝이 아니라, 트렌드에 맞춰 지속적인 업데이트를 지원합니다.'},
                                {icon:'bot', title:'사기 피해', desc:'계약 후 연락 두절이나 추가 비용 요구 없는 투명하고 정직한 파트너가 됩니다.'},
                                {icon:'file-text', title:'소통 불가', desc:'어려운 전문 용어 대신 사장님의 눈높이에서 친절하고 빠른 피드백을 제공합니다.'},
                                {icon:'monitor-off', title:'무료 사기', desc:'무료제작, 3년 약정 후 해지비용 100만원?, 사기꾼들을 피하세요.'},
                                {icon:'tv-minimal-play', title:'간단 업무', desc:'"전화 한 통으로 해결되는 유지보수"는 바쁜 사장님들께 가장 강력한 소구점입니다.'},
                                {icon:'users', title:'자료 부족', desc:'사장님은 아이디어만 주셔도 충분합니다. 나머지는 저희의 몫입니다.'}
						
                            ].map((box, i) => (
                                <div key={i} data-aos="fade-up" data-aos-delay={i*100} className="bg-slate-900 border border-slate-800 p-8 rounded-[2.5rem] hover:border-slate-500 transition group flex items-start gap-6">
                                    <div className="w-16 h-16 bg-slate-800 text-brand-500 rounded-2xl flex items-center justify-center shrink-0 group-hover:bg-brand-600 group-hover:text-white transition"><Icon name={box.icon} size={32} /></div>
                                    <div>
                                        <h4 className="font-black text-slate-100 mb-2 text-xl">{box.title}</h4>
                                        <p className="text-slate-400 text-sm leading-relaxed">{box.desc}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </section>
"""

new_content = before_hero + portfolio_code + problems_code + "\n" + pricing_start_marker + after_pricing

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
    
print("Successfully updated index.html")
