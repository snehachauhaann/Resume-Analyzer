from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import SKILLS

def calculate_similarity(resume, job_desc):

    documents = [resume, job_desc]

    vectorizer = CountVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    similarity = cosine_similarity(vectors)[0][1]

    return round(similarity * 100, 2)


def skill_analysis(resume, job_desc):

    resume = resume.lower()
    job_desc = job_desc.lower()

    matched = []
    missing = []

    for skill in SKILLS:
        if skill in resume and skill in job_desc:
            matched.append(skill)
        elif skill in job_desc and skill not in resume:
            missing.append(skill)

    return matched, missing
