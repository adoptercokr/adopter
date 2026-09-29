import urllib.request
import os
import json

out_dir = "Customer/260930-moheomdam-모험담/img"
os.makedirs(out_dir, exist_ok=True)

# 1. 첫번째 모험 (네이버 예약 공식 10장)
room1_urls = [
    "https://naverbooking-phinf.pstatic.net/20240821_73/1724227127099mfa6K_JPEG/moheomdam_001.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_225/1724227127374bFUg8_JPEG/moheomdam_002.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_30/1724227127662VE1xi_JPEG/moheomdam_003.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_58/1724227127914UzcH6_JPEG/moheomdam_006.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_123/1724227128100j393K_JPEG/moheomdam_007.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_17/1724227128406yxn7c_JPEG/moheomdam_011.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_104/1724227128708TWMsr_JPEG/moheomdam_009.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_227/1724227130507KxJpX_JPEG/265.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_19/17242271297733A2m2_JPEG/252.jpg",
    "https://naverbooking-phinf.pstatic.net/20240821_32/17242271265617hYcR_JPEG/moheomdam_005.jpg"
]

# 2. 두번째 모험 (원형 벽난로 & 패밀리 리빙룸 & 테라스 10장)
room2_urls = [
    "http://blogfiles.naver.net/MjAyNjA1MjZfNTkg/MDAxNzc5Nzc2Nzg4ODA1.685TS0TcZtS3YW4Zi2ZpoGJWXKQguR-EMtr6tbubF3Yg.ckhcrphBR5Slqz_aIkx-1lhqg6b0I21s4LXq84tWKvYg.JPEG/IMG%A3%DF8360.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMzQg/MDAxNzc5Nzc2Nzg5MDU1.oGdtLLSLd8Yd9NLzKdQ7TyZlNSOyxPMRe4uh5JYfam8g.57MAJjrTjv8nbheLPWFaL8SvKUfqrNgjYqMx5-9mdXEg.JPEG/IMG%A3%DF8362.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMjcy/MDAxNzc5Nzc2Nzg2NzUx.laXRI4T581Tbn51pc-_1RqA_W-U1GXvIUomazyU0uYcg.Cf0gJy4SWqmbcZYW67oXY9f7vDrTsVY_Cwy92XTg4dkg.JPEG/IMG%A3%DF8377.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMyAg/MDAxNzc5Nzc2Nzg4ODc2.zZzTnl8w-YHy8IhDGwuQavyM9Q3dXe8FNoE82qxOCLkg.O1ATMcii0iOd1CazCrptbGIjAj05E1rhtdtPVXIyqNgg.JPEG/IMG%A3%DF8375.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMjI1/MDAxNzc5Nzc2Nzg3OTk2.Yytg92OFYI_XM9NxhL-Wh3PLQ-V42rqfY7mt8s0ppR4g.2hjJbvjKJYck8rkLpmFZvvHlvpDGu_7kMW_SGDIhnVIg.JPEG/IMG%A3%DF8378.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMjM0/MDAxNzc5Nzc2Nzg2NzY2.AR8gj2pBVqbB_F2OvsBkZkOyfB14LrJvH8e2wv5-kQIg.m2_tpVhn6emZ0-3OvYR86_sJehxIcx81R51WfgavYX0g.JPEG/IMG%A3%DF8392.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMTg3/MDAxNzc5Nzc2Nzg4Mjc1.ZCohyD8jQ8yXuLfEfTCN9SzV1WZKhP3nne9tr_0KYN0g._s3WE-bi4nrbNacfIVAntia5bMENei71RMNGb-Uxkpcg.JPEG/IMG%A3%DF8397.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMjEg/MDAxNzc5Nzc2Nzg5MjQ2.iAFTMfWYyAPn_QhYwRFwCNl6DTzHvDWTPCcww9-VLa4g.EYTb499pKXJQaVtsbCSXQPH9rZ_DkD6cmpo1N3HHE0kg.JPEG/IMG%A3%DF8380.JPG",
    "http://blogfiles.naver.net/MjAyNjA1MjZfMjY0/MDAxNzc5Nzc2Nzg2NzEx.-OXlT9iB4dBFg9wwcVqr85AKDtUh475HI6gdj2Tmzcgg.c2f_FBDnkDRjHyD0toR7L3AArnCo0nstZzGD5cCxexgg.JPEG/IMG%A3%DF8381.JPG",
    "http://blogfiles.naver.net/MjAyNjA2MTZfMjI4/MDAxNzgxNjEyMzA5OTg1.b4PDpu6xZKckjNUj5rEUYIEd3uWubJv9xMzqH7vW57wg.pdQXONrpBJiHa96KAn_GkYDCmk1UJcEI1etN1p2reBcg.JPEG/fdskje.jpg"
]

# 3. 세번째 모험 (프리미엄 풀빌라 & 야외 온수 자쿠지 & 바베큐장 10장)
room3_urls = [
    "http://blogfiles.naver.net/MjAyNjA5MjVfMTMx/MDAxNzkwMzE5MDEzNDI5.pHCw04fdXMcSFm-OF4bK4kG4PSxxn4JwuiwK6gvcK_Yg.KN_-HxyaSKyaouwzftBhjwsNlmXqeMCztkX1XkVZifMg.JPEG/IMG%A3%DF1189.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMjA5/MDAxNzkwMzE5MDIwNzQ0.wmYH2Y3TOkrvCg_nXt_hlH5x7SZM81biokh9HcC2y5Ag.56cn549XyNaOu02irYF2HWeOVCau2JM0DK4QtXiyZ5Ug.JPEG/IMG%A3%DF1188.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMjM1/MDAxNzkwMzE5MDE1NDUx.L2UuV9Jk0CnQFDgNfTPRDNw2uWlt4IVF1a8VuFq9hmMg.20aHNtqpGsDtQSANLKBThA_8xzvUh9HnMl-_PL2EKTkg.JPEG/IMG%A3%DF4796.jpg",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMTAx/MDAxNzkwMzE5MjY0NTQ0.2bi2QolF6LAjov3m8epkLGAYUQbujIUKxEu7GnDBc9Mg.mQHw0oEMT439WRbp1Bh4bNnDMukY5_F8OMjJwZgF3YUg.JPEG/IMG%A3%DF0773.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMjcz/MDAxNzkwMzE5MjY0NTY1.hekQLBi_ck351DRrQrsM2_B_dGj8sIByHujCIRY533Ag.NGtoP_B8cgCgmiDXenm4AH_a72gLUVMaS__7y1sOwoQg.JPEG/IMG%A3%DF0794.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMjQ4/MDAxNzkwMzE5MjY1Nzgx.Ob8Egt0vBweClzP5qoFqcjE1n7soKO6q4VB9RDa3G84g.3jeAlALc3gIqNhYaHrWyWLBDfCBjz10WEU0EQX1_TTUg.JPEG/IMG%A3%DF0774.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMTg1/MDAxNzkwMzE5MjY2MTE1.ZsscA9S3KGOJ2EPX5BjyRV0mY_vp_oZkYBZqot6V23Eg.RZqSfLvEvICebjZRKnrWS_MrCwUgpuA-MkQx_drsI5Ig.JPEG/IMG%A3%DF0792.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMjYx/MDAxNzkwMzE5ODEyNTA0.3rOgW5-ya-9EGj6M0VTEDcvstfoAvGhgWqUAEarAGR4g.FTsz-fZrlESUjOawXk0fPXG0cCShianrmei8HgiCdiMg.JPEG/IMG%A3%DF1193.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjVfMTQ3/MDAxNzkwMzE5OTgzNTUz.BNsLemGEhYaJQiOrnY2ikUycd6lRTXT9fih3CXOYrHcg.VuuAznmyIp6SROc3vHSLBn0BohNpfIrny7don3r2okYg.JPEG/IMG%A3%DF0775.JPG",
    "http://blogfiles.naver.net/MjAyNjA5MjdfMTMz/MDAxNzkwNDkyNTAyNzEy.eVcA5oNyKiJDG8eXEWarLNj5DpY0mVpX_2GouF_rJ3Mg.QBawyhve4O0LFAHpjfVTmzmgL0gu5MboTLMJ_totgswg.JPEG/IMG%A3%DF1063.JPG"
]

def download_list(urls, prefix):
    for i, u in enumerate(urls):
        fn = f"{prefix}_{i+1}.jpg"
        fp = os.path.join(out_dir, fn)
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                with open(fp, "wb") as f:
                    f.write(data)
                print(f"Downloaded {fn} ({len(data)} bytes)")
        except Exception as e:
            print(f"Failed {fn}: {e}")

print("Downloading room 1 photos...")
download_list(room1_urls, "room1")
print("Downloading room 2 photos...")
download_list(room2_urls, "room2")
print("Downloading room 3 photos...")
download_list(room3_urls, "room3")
print("All room photos downloaded successfully!")
