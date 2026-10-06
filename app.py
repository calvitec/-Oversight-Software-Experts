from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "oversight-software-experts-2026"

COMPANY_INFO = {
    "legal_name": "OVERSIGHT SOFTWARE EXPERTS LLC",
    "entity_number": "0451505802",  # ⚠️ replace with your real state entity number
    "registered": "Washington, USA",
    "registered_agent": "Michael Lanza",
    "registered_office": "12214 SE 95th Way, Newcastle, WA 98056",
    "email": "oversightsoftwareexperts@gmail.com",
    "phone": "+1 (253) 420-8212",
    "business_purpose": (
        "To develop, license, market, and support software applications, "
        "digital platforms, and technology solutions for businesses and consumers."
    ),
}

SERVICES = [
    {
        "id": "custom-software",
        "name": "Custom Software Engineering",
        "icon": "fa-terminal",
        "description": (
            "Tailored applications architected around your exact workflows, "
            "from prototype to production."
        ),
        "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=85",
        "features": [
            "Web & mobile apps",
            "API & backend systems",
            "Cloud-native architecture",
            "Legacy modernization",
        ],
    },
    {
        "id": "ai-model-ops",
        "name": "AI Model Operations",
        "icon": "fa-network-wired",
        "description": (
            "Engineering the pipelines, data flows, and evaluation loops "
            "behind production AI systems."
        ),
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=1200&q=85",
        "features": [
            "Training pipelines",
            "Data labeling ops",
            "Model evaluation",
            "Fine-tuning workflows",
        ],
    },
    {
        "id": "platform-licensing",
        "name": "Platform Licensing",
        "icon": "fa-key",
        "description": (
            "Battle-tested products available for licensing, white-labeling, "
            "and enterprise integration."
        ),
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=85",
        "features": [
            "White-label rights",
            "On-prem deployment",
            "SLA-backed support",
            "Custom integrations",
        ],
    },
    {
        "id": "data-engineering",
        "name": "Data Engineering",
        "icon": "fa-database",
        "description": (
            "Reliable data infrastructure that feeds your products, "
            "analytics, and AI systems."
        ),
        "image": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1200&q=85",
        "features": [
            "ETL pipelines",
            "Data warehousing",
            "Real-time streaming",
            "Quality monitoring",
        ],
    },
]

PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Discovery",
        "description": "Deep-dive workshops to map your goals, constraints, and technical landscape.",
        "icon": "fa-magnifying-glass",
    },
    {
        "number": "02",
        "title": "Blueprint",
        "description": "Architecture, wireframes, and a delivery roadmap you can actually follow.",
        "icon": "fa-pen-ruler",
    },
    {
        "number": "03",
        "title": "Build",
        "description": "Iterative development with weekly demos, tests, and continuous feedback.",
        "icon": "fa-code",
    },
    {
        "number": "04",
        "title": "Launch",
        "description": "Deployment, monitoring, and hands-on support as your product scales.",
        "icon": "fa-rocket",
    },
]

WHY_CHOOSE_US = [
    {
        "title": "Senior-Only Team",
        "description": "Every engineer on your project has shipped production software at scale.",
        "icon": "fa-user-tie",
    },
    {
        "title": "AI-Native Workflows",
        "description": "We use AI in our own engineering — and build it for yours.",
        "icon": "fa-wand-magic-sparkles",
    },
    {
        "title": "Transparent Delivery",
        "description": "Weekly demos, shared boards, no black boxes. You see every step.",
        "icon": "fa-eye",
    },
    {
        "title": "US-Registered Entity",
        "description": "An Illinois LLC with clear contracts and accountable business practices.",
        "icon": "fa-certificate",
    },
]

ABOUT = (
    "OVERSIGHT SOFTWARE EXPERTS LLC is an Illinois-based engineering studio "
    "building software for companies that can't afford to ship broken products. "
    "We design, license, and support custom applications, digital platforms, "
    "and technology solutions for businesses and consumers.\n\n"
    "Beyond our own products, we partner with leading AI organizations — "
    "supplying the specialized engineering talent that trains, evaluates, and "
    "optimizes next-generation models. Our work sits at the seam between "
    "human craft and machine scale: the place where useful software actually "
    "gets made."
)


@app.route("/")
def index():
    return render_template(
        "oversight.html",
        company=COMPANY_INFO,
        about=ABOUT,
        services=SERVICES,
        process_steps=PROCESS_STEPS,
        reasons=WHY_CHOOSE_US,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            return render_template(
                "contact.html",
                company=COMPANY_INFO,
                success=False,
                error="Please provide your name, email, and message.",
                form_data={
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "message": message,
                },
            ), 400

        return render_template(
            "contact.html",
            company=COMPANY_INFO,
            success=True,
            name=name,
            message="Thanks for reaching out. We'll reply within one business day.",
        )

    return render_template(
        "contact.html",
        company=COMPANY_INFO,
        success=False,
        form_data={},
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
