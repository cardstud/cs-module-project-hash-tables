# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open(r'C:/Users/Todd/Desktop/project_hashtables/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt') as c:
    c_text = c.read()

ignored_chars = ['"', "'", ':', ';', ',', '.', '+', '=', '/', '\\', '\n', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&',
'1', '2', '3', '4', '5', '6', '7', '8' ,'9', '0', '?', '!', ' ', '_', '-']

letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B',
'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

num_chars_dict = {}

for char in c_text:
    if char not in ignored_chars:
        if char in num_chars_dict:
            num_chars_dict[char] += 1
        else:
            num_chars_dict[char] = 1

for char in num_chars_dict:
    num_chars_dict[char] = (num_chars_dict[char] / len(c_text)) * 100

sorted_frequency_list = sorted(num_chars_dict.items(), key= lambda x: x[1], reverse=True)
sorted_frequency = []
for tup in sorted_frequency_list:
    sorted_frequency.append(tup[0])

new_text = 'ID EWKKF WDQSMDU ID JCW JIEW XB XSU, OCWD QXXU PIDQ CWDKF JCW NWAXDU KGSWU JCW SMDU, JCWKW SIHWU OIJCID JCW QKWWD QSMUWN XB NCWKOXXU BXKWNJ, DWMK DXJJIDQCME JXOD, M BMEXGN XGJSMO OCXNW DMEW OMN KXYID CXXU. DX MKACWK WHWK SIHWU JCMJ AXGSU NZWWU M QKMF QXXNW NCMBJ OIJC NGAC NPISS MDU AGDDIDQ MN CIN, DXK OWKW JCWKW WHWK NGAC FWXEWD MN JCW NWHWDNAXKW EWKKF EWD JCMJ KXMEWU OIJC CIE JCKXGQC JCW QKWWDOXXU NCMUWN. KIQCJ EWKKISF JCWF UOWSSWU OIJCID JCW UWZJCN XB NCWKOXXU BXKWNJ, NGBBWKIDQ DWIJCWK AMKW DXK OMDJ, YGJ ZMNNIDQ JCW JIEW ID EWKKF QMEWN XB MKACWKF XK YXGJN XB AGUQWS ZSMF, SIHIDQ GZXD JCW PIDQ\'N HWDINXD, OMNCWU UXOD OIJC UKMGQCJN XB MSW XB XAJXYWK YKWOIDQ. DXJ XDSF KXYID CIENWSB YGJ MSS JCW YMDU OWKW XGJSMON MDU UOWSSWU MZMKJ BKXE XJCWK EWD, FWJ JCWF OWKW YWSXHWU YF JCW AXGDJKF ZWXZSW KXGDU MYXGJ, BXK DX XDW WHWK AMEW JX TXSSF KXYID BXK CWSZ ID JIEW XB DWWU MDU OWDJ MOMF MQMID OIJC MD WEZJF BINJ. MDU DXO I OISS JWSS CXO IJ AMEW MYXGJ JCMJ KXYID CXXU BWSS MBXGS XB JCW SMO. OCWD KXYID OMN M FXGJC XB WIQCJWWD, NJXGJ XB NIDWO MDU YXSU XB CWMKJ, JCW NCWKIBB XB DXJJIDQCME ZKXASMIEWU M NCXXJIDQ EMJAC MDU XBBWKWU M ZKIRW XB M YGJJ XB MSW JX OCXNXWHWK NCXGSU NCXXJ JCW YWNJ NCMBJ ID DXJJIDQCMENCIKW. "DXO," VGXJC KXYID, "OISS I QX JXX, BXK BMID OXGSU I UKMO M NJKIDQ BXK JCW YKIQCJ WFWN XB EF SMNN MDU M YGJJ XB QXXU XAJXYWK YKWOIDQ." NX GZ CW QXJ MDU JXXP CIN QXXU NJXGJ FWO YXO MDU M NAXKW XK EXKW XB YKXMU ASXJCFMKU MKKXON, MDU NJMKJWU XBB BKXE SXAPNSWF JXOD JCKXGQC NCWKOXXU BXKWNJ JX DXJJIDQCME. IJ OMN MJ JCW UMOD XB UMF ID JCW EWKKF EMFJIEW, OCWD CWUQWKXON MKW QKWWD MDU BSXOWKN YWUWAP JCW EWMUXON; UMINIWN ZIWU MDU FWSSXO AGAPXX YGUN MDU BMIK ZKIEKXNWN MSS MSXDQ JCW YKIWKF CWUQWN; OCWD MZZSW YGUN YSXNNXE MDU NOWWJ YIKUN NIDQ, JCW SMKP MJ UMOD XB UMF, JCW JCKXNJSW AXAP MDU AGAPXX; OCWD SMUN MDU SMNNWN SXXP GZXD WMAC XJCWK OIJC NOWWJ JCXGQCJN; OCWD YGNF CXGNWOIHWN NZKWMU JCWIK SIDWD JX YSWMAC GZXD JCW YKIQCJ QKWWD QKMNN. NOWWJ OMN JCW QKWWDOXXU MN CW OMSPWU MSXDQ IJN ZMJCN, MDU YKIQCJ JCW QKWWD MDU KGNJSIDQ SWMHWN, MEIU OCIAC JCW SIJJSW YIKUN NMDQ OIJC EIQCJ MDU EMID: MDU YSIJCWSF KXYID OCINJSWU MN CW JKGUQWU MSXDQ, JCIDPIDQ XB EMIU EMKIMD MDU CWK YKIQCJ WFWN, BXK MJ NGAC JIEWN M FXGJC\'N JCXGQCJN MKW OXDJ JX JGKD ZSWMNMDJSF GZXD JCW SMNN JCMJ CW SXHWN JCW YWNJ. MN JCGN CW OMSPWU MSXDQ OIJC M YKINP NJWZ MDU M EWKKF OCINJSW, CW AMEW NGUUWDSF GZXD NXEW BXKWNJWKN NWMJWU YWDWMJC M QKWMJ XMP JKWW. BIBJWWD JCWKW OWKW ID MSS, EMPIDQ JCWENWSHWN EWKKF OIJC BWMNJIDQ MDU UKIDPIDQ MN JCWF NMJ MKXGDU M CGQW ZMNJF, JX OCIAC WMAC EMD CWSZWU CIENWSB, JCKGNJIDQ CIN CMDUN IDJX JCW ZIW, MDU OMNCIDQ UXOD JCMJ OCIAC JCWF MJW OIJC QKWMJ CXKDN XB MSW OCIAC JCWF UKWO MSS BXMEIDQ BKXE M YMKKWS JCMJ NJXXU DIQC. WMAC EMD OMN ASMU ID SIDAXSD QKWWD, MDU M BIDW NCXO JCWF EMUW, NWMJWU GZXD JCW NOMKU YWDWMJC JCMJ BMIK, NZKWMUIDQ JKWW. JCWD XDW XB JCWE, OIJC CIN EXGJC BGSS, AMSSWU XGJ JX KXYID, "CGSSXM, OCWKW QXWNJ JCXG, SIJJSW SMU, OIJC JCF XDW-ZWDDF YXO MDU JCF BMKJCIDQ NCMBJN?" JCWD KXYID QKWO MDQKF, BXK DX NJKIZSIDQ SIPWN JX YW JMGDJWU OIJC CIN QKWWD FWMKN. "DXO," VGXJC CW, "EF YXO MDU WPW EIDW MKKXON MKW MN QXXU MN NCIDW; MDU EXKWXHWK, I QX JX JCW NCXXJIDQ EMJAC MJ DXJJIDQCME JXOD, OCIAC NMEW CMN YWWD ZKXASMIEWU YF XGK QXXU NCWKIBB XB DXJJIDQCMENCIKW; JCWKW I OISS NCXXJ OIJC XJCWK NJXGJ FWXEWD, BXK M ZKIRW CMN YWWD XBBWKWU XB M BIDW YGJJ XB MSW." JCWD XDW OCX CWSU M CXKD XB MSW ID CIN CMDU NMIU, "CX! SINJWD JX JCW SMU! OCF, YXF, JCF EXJCWK\'N EISP IN FWJ NAMKAW UKF GZXD JCF SIZN, MDU FWJ JCXG ZKMJWNJ XB NJMDUIDQ GZ OIJC QXXU NJXGJ EWD MJ DXJJIDQCME YGJJN, JCXG OCX MKJ NAMKAW MYSW JX UKMO XDW NJKIDQ XB M JOX-NJXDW YXO." "I\'SS CXSU JCW YWNJ XB FXG JOWDJF EMKPN," VGXJC YXSU KXYID, "JCMJ I CIJ JCW ASXGJ MJ JCKWWNAXKW KXUN, YF JCW QXXU CWSZ XB XGK SMUF BMIK." MJ JCIN MSS SMGQCWU MSXGU, MDU XDW NMIU, "OWSS YXMNJWU, JCXG BMIK IDBMDJ, OWSS YXMNJWU! MDU OWSS JCXG PDXOWNJ JCMJ DX JMKQWJ IN DIQC JX EMPW QXXU JCF OMQWK." MDU MDXJCWK AKIWU, "CW OISS YW JMPIDQ MSW OIJC CIN EISP DWLJ."'

deciphered_text = ''
for char in new_text:
    if char in sorted_frequency:
        index_char = sorted_frequency.index(char)
        char = letter_frequency[index_char]
        deciphered_text += char
    else:
        deciphered_text += char
        

print(deciphered_text)

