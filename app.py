
import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------
st.title("🚀 SkillBridge AI")
st.subheader("Bridging the Gap Between Education and Employment")

st.write(
    "Discover entry-level career paths, compare your skills "
    "with job requirements, and identify areas for improvement."
)

st.info(
    "SkillBridge AI helps graduates explore career options, "
    "identify skills gaps, and plan their professional development."
)

st.divider()

# --------------------------------------------------
# USER PROFILE
# --------------------------------------------------
st.header("👤 Create Your Career Profile")

name = st.text_input("Your name")

qualification = st.selectbox(
    "Your highest qualification",
    [
        "Matric",
        "Certificate",
        "Diploma",
        "Bachelor's Degree",
        "Honours Degree",
        "Master's Degree",
        "Other"
    ]
)

career = st.selectbox(
    "Which career interests you?",
    [
        "Data Analyst",
        "Data Scientist",
        "Software Developer",
        "Business Intelligence Analyst"
    ]
)

available_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Machine Learning",
    "Git",
    "Communication",
    "Data Analysis"
]

selected_skills = st.multiselect(
    "Select the skills you currently have",
    available_skills
)

# --------------------------------------------------
# ILLUSTRATIVE JOB DATA
# --------------------------------------------------
jobs = [
    {
        "Job Title": "Junior Data Analyst",
        "Career": "Data Analyst",
        "Required Skills": ["Python", "SQL", "Excel", "Power BI"]
    },
    {
        "Job Title": "Junior Data Scientist",
        "Career": "Data Scientist",
        "Required Skills": [
            "Python", "SQL", "Machine Learning", "Data Analysis"
        ]
    },
    {
        "Job Title": "Junior Software Developer",
        "Career": "Software Developer",
        "Required Skills": ["Python", "Git", "SQL"]
    },
    {
        "Job Title": "Business Intelligence Analyst",
        "Career": "Business Intelligence Analyst",
        "Required Skills": [
            "SQL", "Excel", "Power BI", "Data Analysis"
        ]
    }
]

# --------------------------------------------------
# LEARNING RECOMMENDATIONS
# --------------------------------------------------
learning_resources = {
    "Python": (
        "Practise Python programming and build a small project."
    ),
    "SQL": (
        "Learn SELECT, WHERE, JOIN, GROUP BY and aggregate functions."
    ),
    "Excel": (
        "Practise formulas, pivot tables and data cleaning."
    ),
    "Power BI": (
        "Build a dashboard using a public dataset."
    ),
    "Machine Learning": (
        "Study model training, testing and evaluation."
    ),
    "Git": (
        "Practise version control using Git and GitHub."
    ),
    "Communication": (
        "Practise presenting your findings clearly."
    ),
    "Data Analysis": (
        "Complete an exploratory data analysis project."
    )
}

# --------------------------------------------------
# MATCHING ENGINE
# --------------------------------------------------
if st.button("🔍 Find My Job Matches", type="primary"):

    if not name.strip():
        st.warning("Please enter your name.")

    elif not selected_skills:
        st.warning("Please select at least one skill.")

    else:
        user_skills = set(selected_skills)

        # Filter roles according to the selected career.
        relevant_jobs = [
            job for job in jobs
            if job["Career"] == career
        ]

        results = []

        for job in relevant_jobs:

            required_skills = set(job["Required Skills"])

            matched_skills = required_skills.intersection(user_skills)
            missing_skills = required_skills.difference(user_skills)

            score = (
                len(matched_skills) / len(required_skills)
            ) * 100

            results.append({
                "Job Title": job["Job Title"],
                "Match Score (%)": round(score, 1),
                "Matched Skills": (
                    ", ".join(sorted(matched_skills))
                    if matched_skills else "None"
                ),
                "Skills to Develop": (
                    ", ".join(sorted(missing_skills))
                    if missing_skills else "None"
                )
            })

        results_df = pd.DataFrame(results)

        results_df = results_df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        # --------------------------------------------------
        # JOB MATCH RESULTS
        # --------------------------------------------------
        st.success(f"Welcome, {name}!")

        st.subheader("📊 Your Potential Job Matches")

        col1, col2, col3 = st.columns(3)

        best_match = results_df.iloc[0]

        with col1:
            st.metric(
                "Career Selected",
                career
            )

        with col2:
            st.metric(
                "Highest Skills Match",
                f"{best_match['Match Score (%)']}%"
            )

        with col3:
            st.metric(
                "Skills Selected",
                len(user_skills)
            )

        st.dataframe(
            results_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "Match scores represent the proportion of listed required "
            "skills selected by the user. They are not the probability "
            "of getting a job. The roles and requirements are illustrative "
            "examples, not verified live vacancies."
        )

        # --------------------------------------------------
        # PERSONAL LEARNING PLAN
        # --------------------------------------------------
        st.divider()
        st.subheader("💡 Your Personal Learning Plan")

        required_skills = set(
            next(
                job["Required Skills"]
                for job in jobs
                if job["Career"] == career
            )
        )

        missing_skills = required_skills - user_skills

        st.write(
            f"Your strongest skills match is **{best_match['Job Title']}**, "
            f"with a score of **{best_match['Match Score (%)']}%**."
        )

        if missing_skills:

            st.write(
                "Consider the following actions to strengthen your "
                "profile for this career:"
            )

            for skill in sorted(missing_skills):
                st.markdown(f"#### 📚 {skill}")

                st.write(
                    learning_resources.get(
                        skill,
                        "Find a relevant course and practise the skill."
                    )
                )

        else:
            st.success(
                "You selected all the skills listed for this role! "
                "Consider building a project to demonstrate your abilities."
            )

        st.info(
            "These are general learning suggestions, not a guarantee "
            "of employment or a verified assessment of an employer's "
            "requirements."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "SkillBridge AI | FNB App of the Year Hackathon 2026"
)
