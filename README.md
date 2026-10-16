# 🌐 Personal Portfolio Website (Streamlit)

Welcome to the source code repository for my multi-page **Personal Portfolio Website** built with **Streamlit**! This interactive web application showcases my background, AI/ML & engineering projects, astrophotography/extracurricular activities, and an integrated webhook contact form.

---

## 📂 Project Structure

```text
Portfolio-Website/
├── assets/                  # Project screenshots, profile photo, and astrophotography images
├── forms/
│   └── contact.py           # Interactive contact form integrated with webhook notifications
├── styles/
│   └── main.css             # Custom CSS styling injected into Streamlit
├── views/
│   ├── about_me.py          # Hero section, biography, education, and technical skills
│   ├── projects.py          # Showcase of featured AI/ML and software projects with links
│   └── extracurricular.py   # Astrophotography gallery and extracurricular highlights
├── main.py                  # Multi-page Streamlit navigation entrypoint
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## ✨ Features

- **Multi-Page Streamlit Navigation**: Clean sidebar routing across *About Me*, *Projects*, and *Extracurricular* views (`main.py`).
- **Project Showcase**: Highlights flagship projects including *SparshGPT*, *TAAS Discord Bot*, *Ecommerce Regression Analysis*, and *Ocean Escapes* with screenshots and direct links.
- **Astrophotography Gallery**: Displays captured celestial images (Orion Constellation, deep-sky captures).
- **Integrated Contact Form**: Validates user inputs and dispatches messages via `WEBHOOK_URL` configured in Streamlit secrets (`forms/contact.py`).

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sparsh0106/Portfolio-Website.git
   cd Portfolio-Website
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
