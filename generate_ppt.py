import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # completely blank slide

    # Color Palette Definitions
    C_DARK = RGBColor(0x1E, 0x12, 0x0B)        # #1E120B Deep Charcoal Espresso
    C_BG_CREAM = RGBColor(0xFA, 0xF6, 0xF0)    # #FAF6F0 Soft Cream
    C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)       # #FFFFFF Pure White
    C_CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)     # White card
    C_CARD_DARK = RGBColor(0x2B, 0x1B, 0x12)   # Dark Card
    C_BROWN = RGBColor(0x4A, 0x2E, 0x1B)       # #4A2E1B Primary Brown
    C_AMBER = RGBColor(0xD9, 0x77, 0x24)       # #D97724 Accent Amber
    C_GOLD = RGBColor(0xF5, 0x9E, 0x0B)        # #F59E0B Warm Gold
    C_TEXT_DARK = RGBColor(0x2A, 0x1A, 0x12)   # #2A1A12 Dark text
    C_TEXT_MUTED = RGBColor(0x6C, 0x5B, 0x52)  # #6C5B52 Muted Gray-Brown
    C_BORDER = RGBColor(0xE6, 0xDC, 0xD0)      # Subtle Border
    C_GREEN = RGBColor(0x22, 0xC5, 0x5E)       # Green Success
    C_PINK = RGBColor(0xC2, 0x18, 0x5B)        # Wedding Pink

    assets_dir = os.path.abspath("assets")
    logo_path = os.path.join(assets_dir, "logo.jpg")
    mhs_path = os.path.join(assets_dir, "portfolio-mhsadvokat.jpg")
    undangan_path = os.path.join(assets_dir, "portfolio-undangan.jpg")
    kemenangan_path = os.path.join(assets_dir, "portfolio-kemenangan.jpg")
    castelube_path = os.path.join(assets_dir, "portfolio-castelubeindo.jpg")

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text=None, is_dark=False):
        # Section Pill Tag
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(3.2), Inches(0.38))
        tag.fill.solid()
        tag.fill.fore_color.rgb = RGBColor(0x3D, 0x24, 0x19) if is_dark else RGBColor(0xF0, 0xE4, 0xD5)
        tag.line.color.rgb = C_AMBER
        tag.line.width = Pt(1)
        tf_tag = tag.text_frame
        tf_tag.word_wrap = True
        tf_tag.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.bold = True
        p_tag.font.size = Pt(10)
        p_tag.font.color.rgb = C_GOLD if is_dark else C_AMBER
        p_tag.font.name = "Arial"
        p_tag.alignment = PP_ALIGN.CENTER

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.9), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.bold = True
        p_t.font.size = Pt(26)
        p_t.font.color.rgb = C_WHITE if is_dark else C_TEXT_DARK
        p_t.font.name = "Arial"

        # Subtitle if exists
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(11.7), Inches(0.45))
            tf_s = sub_box.text_frame
            tf_s.word_wrap = True
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle_text
            p_s.font.size = Pt(12)
            p_s.font.color.rgb = RGBColor(0xD1, 0xC5, 0xBD) if is_dark else C_TEXT_MUTED
            p_s.font.name = "Calibri"

    # =========================================================================
    # SLIDE 1: COVER SLIDE (DARK THEME)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, C_DARK)

    # Accent decorative banner on top-right
    dec = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(-1.5), Inches(6.5), Inches(6.5))
    dec.fill.solid()
    dec.fill.fore_color.rgb = RGBColor(0x2B, 0x1A, 0x11)
    dec.line.fill.background()

    # Logo
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(1.0), Inches(1.2), Inches(1.4), Inches(1.4))

    # Badge Pill
    badge1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.7), Inches(1.5), Inches(4.2), Inches(0.45))
    badge1.fill.solid()
    badge1.fill.fore_color.rgb = RGBColor(0x35, 0x20, 0x15)
    badge1.line.color.rgb = C_AMBER
    p_b1 = badge1.text_frame.paragraphs[0]
    p_b1.text = "BRWNWEB • WEBSITE CREATION SERVICES"
    p_b1.font.bold = True
    p_b1.font.size = Pt(11)
    p_b1.font.color.rgb = C_GOLD
    p_b1.font.name = "Arial"
    p_b1.alignment = PP_ALIGN.CENTER

    # Main Headline
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(2.9), Inches(10.5), Inches(2.2))
    tf = tbox.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "Jasa Pembuatan Website\nCustom & Professional"
    p1.font.bold = True
    p1.font.size = Pt(40)
    p1.font.color.rgb = C_WHITE
    p1.font.name = "Arial"

    p2 = tf.add_paragraph()
    p2.text = "Solusi Desain Modern, Cepat, Responsif, & Terjangkau untuk Mendongkrak Kredibilitas Bisnis Anda"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(0xD1, 0xC5, 0xBD)
    p2.font.name = "Calibri"
    p2.space_before = Pt(16)

    # Key Stat Badges Row on Cover
    stats_data = [
        ("9+", "Website Selesai"),
        ("99.9%", "Garansi Uptime"),
        ("100%", "Kepuasan Klien"),
        ("1-3 Hari", "Pengerjaan Cepat")
    ]
    for i, (num, lbl) in enumerate(stats_data):
        card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + i*2.7), Inches(5.4), Inches(2.45), Inches(1.2))
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(0x28, 0x18, 0x0F)
        card.line.color.rgb = RGBColor(0x4A, 0x2E, 0x1B)
        tf_c = card.text_frame
        tf_c.word_wrap = True
        p_c1 = tf_c.paragraphs[0]
        p_c1.text = num
        p_c1.font.bold = True
        p_c1.font.size = Pt(22)
        p_c1.font.color.rgb = C_GOLD
        p_c1.alignment = PP_ALIGN.CENTER
        p_c2 = tf_c.add_paragraph()
        p_c2.text = lbl
        p_c2.font.size = Pt(11)
        p_c2.font.color.rgb = RGBColor(0xD1, 0xC5, 0xBD)
        p_c2.alignment = PP_ALIGN.CENTER

    # Footer note on Cover
    fb = s1.shapes.add_textbox(Inches(1.0), Inches(6.8), Inches(11.3), Inches(0.4))
    p_fb = fb.text_frame.paragraphs[0]
    p_fb.text = "🌐 Official Website: https://brwnweb-official.vercel.app/   |   📞 WhatsApp: +62 812-8532-4814"
    p_fb.font.size = Pt(11)
    p_fb.font.color.rgb = RGBColor(0x9E, 0x8D, 0x82)

    # =========================================================================
    # SLIDE 2: TENTANG KAMI & VALUE PROPOSITION
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, C_BG_CREAM)
    add_header(s2, "Profil Bisnis & Nilai Utama", "Mengapa Memilih BRWNWEB?", 
               "Kami hadir memberikan solusi kehadiran digital profesional tanpa biaya membengkak dan tanpa proses rumit.")

    props = [
        ("Desain Modern & Custom", "Bukan sekadar template instan. Setiap website dirancang estetis, mencerminkan identitas brand usaha Anda, dan memberikan impresi pertama yang memukau."),
        ("100% Mobile First Responsive", "Lebih dari 80% calon pembeli mengakses lewat smartphone. Website kami dijamin ringan, rapi, dan responsif di semua perangkat Android & iOS."),
        ("Kecepatan & Tepat Waktu", "Waktu pengerjaan terukur (1-3 hari untuk undangan/portofolio, 3-7 hari untuk company profile) sehingga usaha Anda segera tampil online."),
        ("Free Support & Pendampingan", "Bebas biaya setup dan free pendampingan selama 1 tahun penuh. Tim support siap membantu pertanyaan teknis kapan saja.")
    ]

    for i, (title, desc) in enumerate(props):
        col = i % 2
        row = i // 2
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col * 5.9), Inches(2.2 + row * 2.3), Inches(5.6), Inches(2.05))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        # Number accent circle
        num_circle = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.1 + col * 5.9), Inches(2.45 + row * 2.3), Inches(0.55), Inches(0.55))
        num_circle.fill.solid()
        num_circle.fill.fore_color.rgb = C_AMBER
        num_circle.line.fill.background()
        p_nc = num_circle.text_frame.paragraphs[0]
        p_nc.text = str(i+1)
        p_nc.font.bold = True
        p_nc.font.size = Pt(14)
        p_nc.font.color.rgb = C_WHITE
        p_nc.alignment = PP_ALIGN.CENTER

        # Content Text
        tb = s2.shapes.add_textbox(Inches(1.8 + col * 5.9), Inches(2.35 + row * 2.3), Inches(4.4), Inches(1.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.bold = True
        p_t.font.size = Pt(15)
        p_t.font.color.rgb = C_BROWN
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = C_TEXT_MUTED
        p_d.space_before = Pt(6)

    # =========================================================================
    # SLIDE 3: LAYANAN UTAMA KAMI (5 CORE SERVICES)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, C_BG_CREAM)
    add_header(s3, "Solusi Lengkap", "5 Layanan Pembuatan Website BRWNWEB", 
               "Dirancang khusus untuk menyesuaikan skala dan tujuan bisnis Anda dengan harga transparan.")

    services = [
        ("Company Profile Bisnis", "Website resmi profil perusahaan, kantor hukum, manufaktur, dan instansi untuk membangun trust & kredibilitas."),
        ("Toko Online / E-Commerce", "Katalog produk, harga, deskripsi detail, tombol direct checkout WhatsApp, dan integrasi payment gateway."),
        ("Portofolio & Personal", "Showcase karya, CV online, dan pencapaian personal branding bagi mahasiswa, freelancer, maupun profesional."),
        ("Undangan Digital Modern", "Website undangan pernikahan interaktif lengkap dengan musik, galeri foto, peta Google Maps, RSVP, & amplop online."),
        ("Sistem & Custom Web App", "Aplikasi web khusus seperti dashboard nilai, portal data internal, manajemen pesanan, dan otomasi kerja.")
    ]

    for i, (stitle, sdesc) in enumerate(services):
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 2.38), Inches(2.3), Inches(2.25), Inches(4.4))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_AMBER if i == 0 else C_BORDER
        card.line.width = Pt(1.5 if i == 0 else 1)

        # Top Accent Pill
        pill = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + i * 2.38), Inches(2.55), Inches(1.85), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(0xFE, 0xF3, 0xC7) if i == 0 else RGBColor(0xF0, 0xEA, 0xE1)
        pill.line.fill.background()
        p_p = pill.text_frame.paragraphs[0]
        p_p.text = f"LAYANAN 0{i+1}"
        p_p.font.bold = True
        p_p.font.size = Pt(9)
        p_p.font.color.rgb = C_AMBER
        p_p.alignment = PP_ALIGN.CENTER

        tb = s3.shapes.add_textbox(Inches(0.95 + i * 2.38), Inches(3.1), Inches(1.95), Inches(3.3))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = stitle
        pt.font.bold = True
        pt.font.size = Pt(13)
        pt.font.color.rgb = C_TEXT_DARK
        pd = tf.add_paragraph()
        pd.text = sdesc
        pd.font.size = Pt(10)
        pd.font.color.rgb = C_TEXT_MUTED
        pd.space_before = Pt(10)

    # =========================================================================
    # SLIDE 4: TEKNOLOGI & STANDAR MUTU (TECH STACK)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, C_DARK)
    add_header(s4, "Arsitektur & Standar Mutu", "Teknologi Modern yang Kami Gunakan", 
               "Fondasi kode bersih, keamanan terenkripsi, dan infrastruktur cloud berkecepatan tinggi.", is_dark=True)

    techs = [
        ("HTML5 & Semantic", "Struktur semantik standar W3C ramah Google Bot dan aksesibel."),
        ("CSS3 & Modern Layout", "Flexbox, Grid, micro-animations 60fps, dan dark mode switcher."),
        ("JavaScript (ES6+)", "Logika interaktif dinamis, kalkulator harga, dan modal instan."),
        ("PHP & Backend Engine", "Logika pemrosesan server yang stabil, aman, dan modular."),
        ("Cloud SSD NVMe", "Server berkecepatan tinggi dengan jaminan uptime 99.9% 24/7."),
        ("SSL Security (HTTPS)", "Enkripsi data tingkat tinggi standar bank untuk keamanan transaksi."),
        ("SEO & Analytics", "Meta Title, Description, sitemap XML, dan integrasi Google Search."),
        ("Direct WhatsApp API", "Tombol konsultasi instan & sistem checkout form ke WhatsApp.")
    ]

    for i, (tname, tdesc) in enumerate(techs):
        col = i % 4
        row = i // 4
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col * 2.95), Inches(2.2 + row * 2.3), Inches(2.8), Inches(2.05))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_DARK
        card.line.color.rgb = RGBColor(0x4A, 0x2E, 0x1B)
        card.line.width = Pt(1)

        tb = s4.shapes.add_textbox(Inches(0.95 + col * 2.95), Inches(2.35 + row * 2.3), Inches(2.5), Inches(1.75))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = tname
        pt.font.bold = True
        pt.font.size = Pt(13)
        pt.font.color.rgb = C_GOLD
        pd = tf.add_paragraph()
        pd.text = tdesc
        pd.font.size = Pt(10)
        pd.font.color.rgb = RGBColor(0xD1, 0xC5, 0xBD)
        pd.space_before = Pt(8)

    # =========================================================================
    # SLIDE 5: PORTOFOLIO SHOWCASE 1 - MHS ADVOKAT & KEMENANGAN SIGNATURE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, C_BG_CREAM)
    add_header(s5, "Studi Kasus & Portofolio", "Hasil Pengerjaan Klien Kami (Bagian 1)", 
               "Website live berstandar profesional yang telah aktif digunakan oleh klien:")

    # Card 1: MHS Advokat (Featured Recent)
    c1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_WHITE
    c1.line.color.rgb = C_AMBER
    c1.line.width = Pt(2)

    if os.path.exists(mhs_path):
        s5.shapes.add_picture(mhs_path, Inches(0.95), Inches(2.35), Inches(5.4), Inches(2.6))

    tb_mhs = s5.shapes.add_textbox(Inches(0.95), Inches(5.05), Inches(5.4), Inches(1.8))
    tf_m = tb_mhs.text_frame
    tf_m.word_wrap = True
    pm1 = tf_m.paragraphs[0]
    pm1.text = "PROJEK TERBARU: MHS & Rekan (Kantor Hukum)"
    pm1.font.bold = True
    pm1.font.size = Pt(14)
    pm1.font.color.rgb = C_BROWN
    pm2 = tf_m.add_paragraph()
    pm2.text = "• Kategori: Company Profile Law Firm   |   🌐 mhsadvokat.com\n• Fitur: Bidang keahlian perkara hukum (litigasi & bisnis), profil advokat terpercaya, studi kasus, dan integrasi konsultasi hukum online responsif."
    pm2.font.size = Pt(10)
    pm2.font.color.rgb = C_TEXT_MUTED
    pm2.space_before = Pt(4)

    # Card 2: Kemenangan Signature
    c2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_WHITE
    c2.line.color.rgb = C_BORDER
    c2.line.width = Pt(1)

    if os.path.exists(kemenangan_path):
        s5.shapes.add_picture(kemenangan_path, Inches(6.95), Inches(2.35), Inches(5.4), Inches(2.6))

    tb_kmn = s5.shapes.add_textbox(Inches(6.95), Inches(5.05), Inches(5.4), Inches(1.8))
    tf_k = tb_kmn.text_frame
    tf_k.word_wrap = True
    pk1 = tf_k.paragraphs[0]
    pk1.text = "Kemenangan Signature"
    pk1.font.bold = True
    pk1.font.size = Pt(14)
    pk1.font.color.rgb = C_BROWN
    pk2 = tf_k.add_paragraph()
    pk2.text = "• Kategori: E-Commerce & Toko Emas   |   🌐 kemenangansignature.com\n• Fitur: Platform brand toko emas & perhiasan berlian eksklusif dengan katalog luxury, update harga, serta showcase desain modern berkelas."
    pk2.font.size = Pt(10)
    pk2.font.color.rgb = C_TEXT_MUTED
    pk2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 6: PORTOFOLIO SHOWCASE 2 - CASTELUBEINDO & UNDANGAN DIGITAL
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, C_BG_CREAM)
    add_header(s6, "Studi Kasus & Portofolio", "Hasil Pengerjaan Klien Kami (Bagian 2)", 
               "Portofolio ragam industri dari manufaktur oli industri hingga undangan wedding interaktif:")

    # Card 1: Castelubeindo
    c3 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.8))
    c3.fill.solid()
    c3.fill.fore_color.rgb = C_WHITE
    c3.line.color.rgb = C_BORDER
    c3.line.width = Pt(1)

    if os.path.exists(castelube_path):
        s6.shapes.add_picture(castelube_path, Inches(0.95), Inches(2.35), Inches(5.4), Inches(2.6))

    tb_cas = s6.shapes.add_textbox(Inches(0.95), Inches(5.05), Inches(5.4), Inches(1.8))
    tf_c = tb_cas.text_frame
    tf_c.word_wrap = True
    pc1 = tf_c.paragraphs[0]
    pc1.text = "Castelubeindo (PT Caste Lube Indo)"
    pc1.font.bold = True
    pc1.font.size = Pt(14)
    pc1.font.color.rgb = C_BROWN
    pc2 = tf_c.add_paragraph()
    pc2.text = "• Kategori: Company Profile Industri   |   🌐 castelubeindo.com\n• Fitur: Website profil perusahaan manufaktur dan distributor pelumas industri berskala nasional dengan katalog spesifikasi mesin ISO standard."
    pc2.font.size = Pt(10)
    pc2.font.color.rgb = C_TEXT_MUTED
    pc2.space_before = Pt(4)

    # Card 2: Undangan Wedding Digital
    c4 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.8))
    c4.fill.solid()
    c4.fill.fore_color.rgb = C_WHITE
    c4.line.color.rgb = C_PINK
    c4.line.width = Pt(1.5)

    if os.path.exists(undangan_path):
        s6.shapes.add_picture(undangan_path, Inches(6.95), Inches(2.35), Inches(5.4), Inches(2.6))

    tb_und = s6.shapes.add_textbox(Inches(6.95), Inches(5.05), Inches(5.4), Inches(1.8))
    tf_u = tb_und.text_frame
    tf_u.word_wrap = True
    pu1 = tf_u.paragraphs[0]
    pu1.text = "Undangan Wedding Digital Modern"
    pu1.font.bold = True
    pu1.font.size = Pt(14)
    pu1.font.color.rgb = C_PINK
    pu2 = tf_u.add_paragraph()
    pu2.text = "• Kategori: Undangan Digital (Rp 100rb)   |   🌐 Live Demo Active\n• Fitur: Desain romantis premium, musik latar audio otomatis, peta lokasi Google Maps, countdown hari H, RSVP form, dan amplop transfer digital."
    pu2.font.size = Pt(10)
    pu2.font.color.rgb = C_TEXT_MUTED
    pu2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 7: PAKET & ESTIMASI BIAYA (PRICING TIERS)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, C_BG_CREAM)
    add_header(s7, "Investasi Transparan", "Pilihan Paket Pembuatan Website", 
               "Biaya masuk akal, tanpa biaya tersembunyi, dan disesuaikan dengan kebutuhan usaha Anda:")

    packages = [
        ("UNDANGAN DIGITAL", "Rp 100.000", "sekali bayar", "1 Halaman interaktif, musik backsound, galeri, Google Maps, RSVP, amplop digital.", False),
        ("PORTOFOLIO", "Rp 500.000", "sekali bayar", "1-2 Halaman profil personal / CV ringkas, showcase portofolio karya, kontak WhatsApp.", False),
        ("STARTER UMKM", "Rp 3.000.000", "/ tahun", "Up to 5 Halaman custom, FREE Domain .com 1 Thn, FREE Cloud SSD 1 Thn, SSL, 1 Email.", False),
        ("BUSINESS ⭐", "Rp 5.000.000", "/ tahun", "Up to 10 Halaman lengkap, FREE Domain & SSD Cloud 1 Thn, SEO On-Page, 3 Email Bisnis.", True),
        ("PROFESSIONAL", "Rp 10.000.000", "/ tahun", "Up to 20 Halaman dynamic, High-Performance Cloud, Advanced SEO, Proteksi Anti-DDoS.", False),
        ("ENTERPRISE", "Rp 15.000.000", "/ tahun", "Full Web App / E-Commerce, Payment Gateway, Dashboard Admin Custom, Dedicated Support.", False)
    ]

    for i, (pname, price, period, pdesc, is_hi) in enumerate(packages):
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 1.98), Inches(2.3), Inches(1.88), Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(0xFE, 0xF3, 0xC7) if is_hi else C_WHITE
        card.line.color.rgb = C_AMBER if is_hi else C_BORDER
        card.line.width = Pt(2 if is_hi else 1)

        # Ribbon for featured
        if is_hi:
            rib = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95 + i * 1.98), Inches(2.45), Inches(1.58), Inches(0.3))
            rib.fill.solid()
            rib.fill.fore_color.rgb = C_AMBER
            rib.line.fill.background()
            p_rib = rib.text_frame.paragraphs[0]
            p_rib.text = "TERFAVORIT ⭐"
            p_rib.font.bold = True
            p_rib.font.size = Pt(8)
            p_rib.font.color.rgb = C_WHITE
            p_rib.alignment = PP_ALIGN.CENTER

        tb = s7.shapes.add_textbox(Inches(0.88 + i * 1.98), Inches(2.8 if is_hi else 2.5), Inches(1.72), Inches(3.8))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = pname
        pt.font.bold = True
        pt.font.size = Pt(11)
        pt.font.color.rgb = C_BROWN

        pp = tf.add_paragraph()
        pp.text = price
        pp.font.bold = True
        pp.font.size = Pt(15)
        pp.font.color.rgb = C_AMBER if is_hi else C_TEXT_DARK
        pp.space_before = Pt(4)

        pper = tf.add_paragraph()
        pper.text = period
        pper.font.size = Pt(9)
        pper.font.color.rgb = C_TEXT_MUTED

        pd = tf.add_paragraph()
        pd.text = pdesc
        pd.font.size = Pt(9)
        pd.font.color.rgb = C_TEXT_MUTED
        pd.space_before = Pt(10)

    # =========================================================================
    # SLIDE 8: FITUR GRATIS YANG SUDAH TERMASUK (ALL-IN BENEFITS)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, C_BG_CREAM)
    add_header(s8, "Nilai Tambah Spesial", "Semua Paket Bisnis Sudah Termasuk:", 
               "Anda tidak perlu membayar biaya terpisah untuk server, domain, keamanan, dan pemeliharaan.")

    benefits = [
        ("FREE Nama Domain Resmi", "Mendapatkan domain resmi (.com / .id / .my.id) gratis selama 1 tahun pertama tanpa biaya registrasi."),
        ("FREE Server Cloud SSD 1 Tahun", "Website di-hosting di server cloud SSD NVMe berkecepatan tinggi dengan jaminan aktif 24 jam non-stop."),
        ("FREE Sertifikat Keamanan SSL", "Enkripsi HTTPS bersertifikat resmi agar website aman dari bahaya siber dan bertanda gembok hijau aman di Google."),
        ("FREE Alamat Email Bisnis", "Email resmi sesuai domain (contoh: info@bisnisanda.com) untuk memperkuat citra profesional brand."),
        ("FREE Basic Image & Logo Editing", "Bantuan merapikan foto produk, kompresi gambar agar loading super cepat, dan penyesuaian logo usaha."),
        ("FREE Maintenance & Garansi", "Pemeliharaan teknis rutin selama 1 tahun penuh untuk memastikan website selalu stabil dan bebas kendala.")
    ]

    for i, (btitle, bdesc) in enumerate(benefits):
        col = i % 3
        row = i // 3
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col * 3.93), Inches(2.3 + row * 2.3), Inches(3.7), Inches(2.05))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        # Check badge
        chk = s8.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.05 + col * 3.93), Inches(2.55 + row * 2.3), Inches(0.45), Inches(0.45))
        chk.fill.solid()
        chk.fill.fore_color.rgb = RGBColor(0xDC, 0xFC, 0xE7)
        chk.line.color.rgb = C_GREEN
        p_c = chk.text_frame.paragraphs[0]
        p_c.text = "✓"
        p_c.font.bold = True
        p_c.font.size = Pt(13)
        p_c.font.color.rgb = C_GREEN
        p_c.alignment = PP_ALIGN.CENTER

        tb = s8.shapes.add_textbox(Inches(1.6 + col * 3.93), Inches(2.45 + row * 2.3), Inches(2.75), Inches(1.75))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = btitle
        pt.font.bold = True
        pt.font.size = Pt(13)
        pt.font.color.rgb = C_BROWN
        pd = tf.add_paragraph()
        pd.text = bdesc
        pd.font.size = Pt(10)
        pd.font.color.rgb = C_TEXT_MUTED
        pd.space_before = Pt(6)

    # =========================================================================
    # SLIDE 9: ALUR KERJA PENGERJAAN (4 LANGKAH MUDAH)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, C_DARK)
    add_header(s9, "Transparan & Praktis", "4 Langkah Mudah Memulai Website Anda", 
               "Proses pemesanan mudah, alur pengerjaan jelas, dan hasil dapat langsung direview sebelum go-live.", is_dark=True)

    steps = [
        ("Langkah 1", "Konsultasi & Pilih Paket", "Diskusikan kebutuhan website dan target audiens bisnis Anda melalui WhatsApp untuk memilih paket yang paling tepat."),
        ("Langkah 2", "Kirimkan Logo & Materi", "Kirimkan materi logo, foto produk, dan profil usaha. Belum ada materi? Tim kami siap membantu menyusunnya."),
        ("Langkah 3", "Pengerjaan & Review", "Website dibangun dalam 2 - 7 hari kerja. Anda mendapatkan link draft online untuk direview dan disesuaikan."),
        ("Langkah 4", "Pelunasan & Website Live!", "Setelah hasil disetujui, domain resmi diaktifkan dan website Anda siap dipromosikan ke seluruh dunia.")
    ]

    for i, (snum, stitle, sdesc) in enumerate(steps):
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 2.95), Inches(2.4), Inches(2.8), Inches(4.3))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_DARK
        card.line.color.rgb = RGBColor(0x4A, 0x2E, 0x1B)
        card.line.width = Pt(1)

        # Number Badge
        nb = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05 + i * 2.95), Inches(2.65), Inches(2.3), Inches(0.45))
        nb.fill.solid()
        nb.fill.fore_color.rgb = C_AMBER
        nb.line.fill.background()
        p_n = nb.text_frame.paragraphs[0]
        p_n.text = snum.upper()
        p_n.font.bold = True
        p_n.font.size = Pt(11)
        p_n.font.color.rgb = C_WHITE
        p_n.alignment = PP_ALIGN.CENTER

        tb = s9.shapes.add_textbox(Inches(1.0 + i * 2.95), Inches(3.3), Inches(2.4), Inches(3.2))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = stitle
        pt.font.bold = True
        pt.font.size = Pt(14)
        pt.font.color.rgb = C_WHITE
        pd = tf.add_paragraph()
        pd.text = sdesc
        pd.font.size = Pt(11)
        pd.font.color.rgb = RGBColor(0xD1, 0xC5, 0xBD)
        pd.space_before = Pt(12)

    # =========================================================================
    # SLIDE 10: KONTAK KONSULTASI & CALL TO ACTION (CLOSING)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, C_BG_CREAM)
    add_header(s10, "Hubungi Tim Kami", "Mulai Konsultasi Website Bisnis Anda Hari Ini", 
               "Tim konsultan kami siap berdiskusi langsung untuk merancang website terbaik sesuai kebutuhan usaha Anda.")

    contacts = [
        ("JEVON", "Konsultan Utama BRWNWEB", "+62 812-8532-4814", "Lead Web Developer & Architecture"),
        ("AMOZ", "Tim Konsultasi BRWNWEB", "+62 813-1609-8209", "Client Relation & Project Consultant"),
        ("TAMARA", "Tim Konsultasi BRWNWEB", "+62 857-8222-8570", "Customer Support & Content Advisor")
    ]

    for i, (name, role, phone, sub) in enumerate(contacts):
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 3.93), Inches(2.3), Inches(3.7), Inches(3.4))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_AMBER if i == 0 else C_BORDER
        card.line.width = Pt(2 if i == 0 else 1)

        # Avatar circle
        av = s10.shapes.add_shape(MSO_SHAPE.OVAL, Inches(2.25 + i * 3.93), Inches(2.6), Inches(0.8), Inches(0.8))
        av.fill.solid()
        av.fill.fore_color.rgb = C_AMBER if i == 0 else RGBColor(0xFA, 0xED, 0xCD)
        av.line.fill.background()
        p_av = av.text_frame.paragraphs[0]
        p_av.text = name[:2]
        p_av.font.bold = True
        p_av.font.size = Pt(14)
        p_av.font.color.rgb = C_WHITE if i == 0 else C_BROWN
        p_av.alignment = PP_ALIGN.CENTER

        tb = s10.shapes.add_textbox(Inches(0.95 + i * 3.93), Inches(3.55), Inches(3.4), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = name
        pt.font.bold = True
        pt.font.size = Pt(17)
        pt.font.color.rgb = C_BROWN
        pt.alignment = PP_ALIGN.CENTER

        pr = tf.add_paragraph()
        pr.text = role
        pr.font.size = Pt(11)
        pr.font.color.rgb = C_TEXT_MUTED
        pr.alignment = PP_ALIGN.CENTER
        pr.space_before = Pt(2)

        pp = tf.add_paragraph()
        pp.text = phone
        pp.font.bold = True
        pp.font.size = Pt(14)
        pp.font.color.rgb = C_GREEN
        pp.alignment = PP_ALIGN.CENTER
        pp.space_before = Pt(8)

        ps = tf.add_paragraph()
        ps.text = sub
        ps.font.size = Pt(10)
        ps.font.color.rgb = C_TEXT_MUTED
        ps.alignment = PP_ALIGN.CENTER
        ps.space_before = Pt(4)

    # Bottom CTA Box
    cta_box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.95), Inches(11.73), Inches(1.1))
    cta_box.fill.solid()
    cta_box.fill.fore_color.rgb = C_DARK
    cta_box.line.color.rgb = C_AMBER
    cta_box.line.width = Pt(1)

    tf_cta = cta_box.text_frame
    tf_cta.word_wrap = True
    p_cta1 = tf_cta.paragraphs[0]
    p_cta1.text = "Siap Membuat Website Impian Bisnis Anda?"
    p_cta1.font.bold = True
    p_cta1.font.size = Pt(15)
    p_cta1.font.color.rgb = C_GOLD
    p_cta1.alignment = PP_ALIGN.CENTER

    p_cta2 = tf_cta.add_paragraph()
    p_cta2.text = "Kunjungi Live Website: https://brwnweb-official.vercel.app/   |   Konsultasi Gratis via WhatsApp 24/7"
    p_cta2.font.size = Pt(12)
    p_cta2.font.color.rgb = C_WHITE
    p_cta2.alignment = PP_ALIGN.CENTER
    p_cta2.space_before = Pt(4)

    # Save Presentation
    output_filename = "BRWNWEB_Company_Profile.pptx"
    prs.save(output_filename)
    print(f"Presentation saved successfully to {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    create_deck()
