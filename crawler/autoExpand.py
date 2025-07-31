def expand_targets(base_urls, targets_file="targets.txt"):
    import re, requests
    from stem.control import Controller

    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    found_links = set()

    for url in base_urls:
        try:
            res = session.get(url, timeout=10)
            matches = re.findall(r"http[s]?://[a-zA-Z0-9]{16,56}\.onion", res.text)
            found_links.update(matches)
        except Exception as e:
            print(f"[!] Failed to scrape seed URL {url}: {e}")

    # Load existing
    try:
        with open(targets_file, 'r') as f:
            existing = set(line.strip().split()[0] for line in f if line.strip())
    except FileNotFoundError:
        existing = set()

    new_links = found_links - existing

    with open(targets_file, 'a') as f:
        for link in new_links:
            f.write(f"{link}  # auto-discovered\n")

    print(f"[+] Added {len(new_links)} new .onion links to {targets_file}")


seed_sources = [
    "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion",
    "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/",
    "http://torlinksge6enmcyyuxjpjkoouw4oorgdgeo7ftnq3zodj7g2zxi3kyd.onion/",
    "http://ctmrktxxkrmu23xdvadockv2rjrou7daomrejw2iaczrw7yvc5lhttqd.onion",
    "http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion",
    "http://uoxqi4lrfqztugili7zzgygibs4xstehf5hohtkpyqcoyryweypzkwid.onion",
    "http://fakeid6mmmaqes6odqilvawtfkfwydu47a2cp77uvtrxck5m4p6wo6yd.onion",
    "http://imperialk4trdzxnpogppugbugvtce3yif62zsuyd2ag5y3fztlurwyd.onion",
    "http://oju4yn237c6hjh42qothvpreqecnqjhtvh4sgn3fqmsdvhu5d5tyspid.onion",
    "http://storexuqpa5j44scdnem6n6etfqwnka4hvw4l3cv566dsldbfrit6eqd.onion",
    "http://cbsrdi4vw4orqehzp2f4a4z36pmqbr2jsbf3piofifncqdnbx6movryd.onion",
    "http://tortimeswqlzti2aqbjoieisne4ubyuoeiiugel2layyudcfrwln76qd.onion",
    "http://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion",
    "http://cebulka7uxchnbpvmqapg5pfos4ngaxglsktzvha7a5rigndghvadeyd.onion",
    "http://czoomdexstp363nde3kf7hp46ptfv7ltgbwjglbd2d3f2ynolc2fpwqd.onion",
    "http://sipulitiepbdalnatudqhfp3gngna37xylawfnk4ywk2ohm64c2mfayd.onion",
    "http://hell2ker5i3xsy6szrl2pulaqo3jhcz6pt7ffdxtuqjqiycvmlkcddqd.onion",
    "http://kowloon5ddwuqwlqckuibv4fxw6m3a6ymk5kinigbjsgjcly346dh7qd.onion",
    "http://piratebayo3klnzokct3wt5yyxb2vpebbuyjl7m623iaxmqhsd52coid.onion",
    "http://bepig5bcjdhtlwpgeh3w42hffftcqmg7b77vzu7ponty52kiey5ec4ad.onion",
    "http://lpiyu33yusoalp5kh3f4hak2so2sjjvjw5ykyvu2dulzosgvuffq6sad.onion",
    "http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion",
    "http://w4ljqtyjnxinknz4hszn4bsof7zhfy5z2h4srfss4vvkoikiwz36o3id.onion",
    "http://hssza6r6fbui4x452ayv3dkeynvjlkzllezxf3aizxppmcfmz2mg7uad.onion",
    "http://x4ijfwy76n6jl7rs4qyhe6qi5rv6xyuos3kaczgjpjcajigjzk3k7wqd.onion",
    "http://superkuhf6grlngvhaelkgaem6i4phmzd7rekeguphwbplhk3fanpjqd.onion",
    "http://count2vxqhf7r4wvhqbaueimgfdp73f6xbawwe2dvkxcso7t475j45ad.onion",
    "http://incoghostm2dytlqdiaj3lmtn7x2l5gb76jhabb6ywbqhjfzcoqq6aad.onion",
    "http://7waci3lpg2exi5njh47eabg6ssdq6dbcpdd3jroomh2jfkx64rigppyd.onion",
    "http://vf7vsrexwb7e4j65idp4hq4eqlvjiwrnvi3jnb4st7oteer5tzgvhaqd.onion",
    "http://dwtqmjzvn2c6z2x462mmbd34ugjjrodowtul4jfbkexjuttzaqzcjyad.onion",
    "http://bbzzzsvqcrqtki6umym6itiixfhni37ybtt7mkbjyxn2pgllzxf2qgyd.onion",
    "http://kiwifarmsaaf4t2h7gc3dfc5ojhmqruw2nit3uejrpiagrxeuxiyxcyd.onion",
    "http://njallalafimoej5i4eg7vlnqjvmb6zhdh27qxcatdn647jtwwwui3nad.onion",
    "http://kingxgja6o7zl3fyiuw2cafyuwp2lfxhoozs3lj2sdftdfzb53hy5zqd.onion",
    "http://awsvrc7occzj2yeyqevyrw7ji5ejuyofhfomidhh5qnuxpvwsucno7id.onion",
    "http://cardedstpc2w3yundoap56eniappn45ll6hfxj2iadmcklc4kldjv4yd.onion",
    "http://rutordeepkpafpudl22pbbhzm4llbgncunvgcc66kax55sc4mp4kxcid.onion",
    "http://rurcblzhmdk22kttfkel2zduhyu3r6to7knyc7wiorzrx5gw4c3lftad.onion",
    "http://gpvdip7rd7bdy5gf7scl3rzgzgzckqw4sqxbmy6g3zijfwu4lz3ypbyd.onion",
    "http://privexioc67u24lsmssoeixnml2exr3les4pbtyqtmv3zvonvcc72jyd.onion",
    "http://spore64i5sofqlfz5gq2ju4msgzojjwifls7rok2cti624zyq3fcelad.onion",
    "http://sharksp64elqkesxjgnwd73qqje3mpvhploeunhpyo6g745mgrayl2qd.onion"
]

expand_targets(seed_sources)
