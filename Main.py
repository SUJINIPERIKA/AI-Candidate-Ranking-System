{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SMVmWO075Ynp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "56c8ebfa-0a8c-4ec9-c88f-7666afc0ce28"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m18.5/18.5 MB\u001b[0m \u001b[31m100.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m253.0/253.0 kB\u001b[0m \u001b[31m18.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install sentence-transformers faiss-cpu python-docx tqdm pandas numpy -q"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "from docx import Document\n",
        "\n",
        "# Load sample candidates\n",
        "with open(\"sample_candidates.json\", \"r\", encoding=\"utf-8\") as f:\n",
        "    candidates = json.load(f)\n",
        "\n",
        "    print(\"Total candidates:\", len(candidates))\n",
        "    print(\"\\nCandidate Keys:\")\n",
        "    print(candidates[0].keys())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "55NfvNbH9ROi",
        "outputId": "408353e0-8117-4164-b1bc-c614e2f94c27"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total candidates: 50\n",
            "\n",
            "Candidate Keys:\n",
            "dict_keys(['candidate_id', 'profile', 'career_history', 'education', 'skills', 'certifications', 'languages', 'redrob_signals'])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pprint\n",
        "\n",
        "pp = pprint.PrettyPrinter(depth=3)\n",
        "pp.pprint(candidates[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q8dPdvUR9cCd",
        "outputId": "ef53a730-8d51-49db-e3d0-8fc0a36e0468"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'candidate_id': 'CAND_0000001',\n",
            " 'career_history': [{'company': 'Mindtree',\n",
            "                     'company_size': '10001+',\n",
            "                     'description': 'Implemented streaming data pipelines on '\n",
            "                                    'Kafka and Spark Streaming for a real-time '\n",
            "                                    'user-activity processing platform. '\n",
            "                                    'Designed the schema-registry integration, '\n",
            "                                    'the watermark/state management approach, '\n",
            "                                    'and the deduplication logic for '\n",
            "                                    'late-arriving events. Worked closely with '\n",
            "                                    'the data science team to make sure '\n",
            "                                    'feature pipelines aligned with what their '\n",
            "                                    'models needed. Most of my career has been '\n",
            "                                    'data engineering, with some adjacent ML '\n",
            "                                    'exposure.',\n",
            "                     'duration_months': 27,\n",
            "                     'end_date': None,\n",
            "                     'industry': 'IT Services',\n",
            "                     'is_current': True,\n",
            "                     'start_date': '2024-03-08',\n",
            "                     'title': 'Backend Engineer'},\n",
            "                    {'company': 'Dunder Mifflin',\n",
            "                     'company_size': '201-500',\n",
            "                     'description': 'Built and maintained data pipelines on '\n",
            "                                    'Apache Airflow processing ~500GB of daily '\n",
            "                                    'transactional data across 12 source '\n",
            "                                    'systems. Worked extensively with Spark '\n",
            "                                    '(PySpark) for batch processing and dbt '\n",
            "                                    'for the transformation/modeling layer in '\n",
            "                                    'our Snowflake warehouse. Owned the '\n",
            "                                    'on-call rotation for data quality issues '\n",
            "                                    '— wrote most of the data quality checks '\n",
            "                                    'that detect schema drift and unusual '\n",
            "                                    'volume changes. The pipeline supports the '\n",
            "                                    'analytics team and a few internal ML '\n",
            "                                    'models.',\n",
            "                     'duration_months': 55,\n",
            "                     'end_date': '2024-01-08',\n",
            "                     'industry': 'Paper Products',\n",
            "                     'is_current': False,\n",
            "                     'start_date': '2019-07-03',\n",
            "                     'title': 'Analytics Engineer'}],\n",
            " 'certifications': [],\n",
            " 'education': [{'degree': 'B.E.',\n",
            "                'end_year': 2020,\n",
            "                'field_of_study': 'Computer Science',\n",
            "                'grade': '8.24 CGPA',\n",
            "                'institution': 'Lovely Professional University',\n",
            "                'start_year': 2017,\n",
            "                'tier': 'tier_3'}],\n",
            " 'languages': [{'language': 'English', 'proficiency': 'professional'},\n",
            "               {'language': 'Hindi', 'proficiency': 'conversational'}],\n",
            " 'profile': {'anonymized_name': 'Ira Vora',\n",
            "             'country': 'Canada',\n",
            "             'current_company': 'Mindtree',\n",
            "             'current_company_size': '10001+',\n",
            "             'current_industry': 'IT Services',\n",
            "             'current_title': 'Backend Engineer',\n",
            "             'headline': 'Backend Engineer | SQL, Spark, Cloud',\n",
            "             'location': 'Toronto',\n",
            "             'summary': 'Software / data professional with 6.9 years of '\n",
            "                        'experience building data pipelines, backend systems, '\n",
            "                        \"and analytics infrastructure. I'm a backend/data \"\n",
            "                        'hybrid — Spark, Airflow, SQL warehouses are home '\n",
            "                        \"territory; I'm building competence on the ML side. My \"\n",
            "                        'toolkit is solid on the data engineering side — '\n",
            "                        'Python, SQL, Spark, Airflow, warehouse design — and '\n",
            "                        \"I've completed a couple of self-directed ML projects \"\n",
            "                        '(Kaggle competitions, side projects fine-tuning small '\n",
            "                        'models). Interested in transitioning toward more '\n",
            "                        'AI/ML-focused work, ideally at a company where I can '\n",
            "                        'leverage my existing data-infra skills while learning '\n",
            "                        'modern ML practice.',\n",
            "             'years_of_experience': 6.9},\n",
            " 'redrob_signals': {'applications_submitted_30d': 2,\n",
            "                    'avg_response_time_hours': 177.8,\n",
            "                    'connection_count': 356,\n",
            "                    'endorsements_received': 35,\n",
            "                    'expected_salary_range_inr_lpa': {'max': 36.1, 'min': 18.7},\n",
            "                    'github_activity_score': 9.2,\n",
            "                    'interview_completion_rate': 0.71,\n",
            "                    'last_active_date': '2026-05-20',\n",
            "                    'linkedin_connected': False,\n",
            "                    'notice_period_days': 60,\n",
            "                    'offer_acceptance_rate': 0.58,\n",
            "                    'open_to_work_flag': True,\n",
            "                    'preferred_work_mode': 'onsite',\n",
            "                    'profile_completeness_score': 86.9,\n",
            "                    'profile_views_received_30d': 23,\n",
            "                    'recruiter_response_rate': 0.34,\n",
            "                    'saved_by_recruiters_30d': 4,\n",
            "                    'search_appearance_30d': 249,\n",
            "                    'signup_date': '2025-10-16',\n",
            "                    'skill_assessment_scores': {'Fine-tuning LLMs': 41.6,\n",
            "                                                'Image Classification': 64.8,\n",
            "                                                'NLP': 38.8,\n",
            "                                                'Speech Recognition': 53.7},\n",
            "                    'verified_email': True,\n",
            "                    'verified_phone': True,\n",
            "                    'willing_to_relocate': False},\n",
            " 'skills': [{'duration_months': 13,\n",
            "             'endorsements': 3,\n",
            "             'name': 'Tailwind',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 26,\n",
            "             'endorsements': 37,\n",
            "             'name': 'NLP',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 40,\n",
            "             'endorsements': 7,\n",
            "             'name': 'Image Classification',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 36,\n",
            "             'endorsements': 21,\n",
            "             'name': 'Fine-tuning LLMs',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 30,\n",
            "             'endorsements': 13,\n",
            "             'name': 'Weights & Biases',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 33,\n",
            "             'endorsements': 52,\n",
            "             'name': 'Speech Recognition',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 24,\n",
            "             'endorsements': 8,\n",
            "             'name': 'Photoshop',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 60,\n",
            "             'endorsements': 56,\n",
            "             'name': 'TTS',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 28,\n",
            "             'endorsements': 0,\n",
            "             'name': 'LoRA',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 9,\n",
            "             'endorsements': 4,\n",
            "             'name': 'Apache Beam',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 8,\n",
            "             'endorsements': 5,\n",
            "             'name': 'AWS',\n",
            "             'proficiency': 'beginner'},\n",
            "            {'duration_months': 15,\n",
            "             'endorsements': 15,\n",
            "             'name': 'Flask',\n",
            "             'proficiency': 'beginner'},\n",
            "            {'duration_months': 36,\n",
            "             'endorsements': 3,\n",
            "             'name': 'BentoML',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 35,\n",
            "             'endorsements': 40,\n",
            "             'name': 'Milvus',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 19,\n",
            "             'endorsements': 12,\n",
            "             'name': 'GANs',\n",
            "             'proficiency': 'advanced'},\n",
            "            {'duration_months': 8,\n",
            "             'endorsements': 9,\n",
            "             'name': 'Statistical Modeling',\n",
            "             'proficiency': 'intermediate'},\n",
            "            {'duration_months': 2,\n",
            "             'endorsements': 7,\n",
            "             'name': 'GCP',\n",
            "             'proficiency': 'beginner'}]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "JOB = {\n",
        "    \"required_skills\": [\n",
        "        \"Python\",\n",
        "        \"SQL\",\n",
        "        \"Spark\",\n",
        "        \"Machine Learning\",\n",
        "        \"NLP\",\n",
        "        \"Fine-tuning LLMs\",\n",
        "        \"MLOps\",\n",
        "        \"Milvus\",\n",
        "        \"FAISS\"\n",
        "    ],\n",
        "    \"min_experience\": 5\n",
        "}\n",
        "\n",
        "\n",
        "def score_candidate(c):\n",
        "\n",
        "    skills = {x[\"name\"].lower() for x in c[\"skills\"]}\n",
        "    required = {x.lower() for x in JOB[\"required_skills\"]}\n",
        "\n",
        "    matched = skills & required\n",
        "    skill_score = len(matched) / len(required) * 100\n",
        "\n",
        "    exp = c[\"profile\"][\"years_of_experience\"]\n",
        "    exp_score = min(exp / 8 * 100, 100)\n",
        "\n",
        "    rr = c[\"redrob_signals\"]\n",
        "\n",
        "    behavior_score = (\n",
        "        rr[\"profile_completeness_score\"] * 0.3 +\n",
        "        rr[\"interview_completion_rate\"] * 30 +\n",
        "        rr[\"github_activity_score\"] * 2 +\n",
        "        rr[\"recruiter_response_rate\"] * 20\n",
        "    )\n",
        "\n",
        "    final_score = (\n",
        "        0.5 * skill_score +\n",
        "        0.3 * exp_score +\n",
        "        0.2 * behavior_score\n",
        "    )\n",
        "\n",
        "    return {\n",
        "        \"id\": c[\"candidate_id\"],\n",
        "        \"name\": c[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": c[\"profile\"][\"current_title\"],\n",
        "        \"score\": round(final_score, 2),\n",
        "        \"matched\": list(matched)\n",
        "    }\n",
        "\n",
        "\n",
        "results = [score_candidate(c) for c in candidates]\n",
        "results.sort(key=lambda x: x[\"score\"], reverse=True)\n",
        "\n",
        "for i, r in enumerate(results[:5], 1):\n",
        "    print(f\"\\nRank {i}\")\n",
        "    print(r)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ysbCkBVj-Up3",
        "outputId": "37741c12-3f76-4fad-d728-6fe3964725f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Rank 1\n",
            "{'id': 'CAND_0000031', 'name': 'Ela Singh', 'title': 'Recommendation Systems Engineer', 'score': 64.45, 'matched': ['faiss', 'mlops', 'machine learning']}\n",
            "\n",
            "Rank 2\n",
            "{'id': 'CAND_0000024', 'name': 'Rajesh Arora', 'title': 'HR Manager', 'score': 57.91, 'matched': []}\n",
            "\n",
            "Rank 3\n",
            "{'id': 'CAND_0000001', 'name': 'Ira Vora', 'title': 'Backend Engineer', 'score': 57.06, 'matched': ['nlp', 'fine-tuning llms', 'milvus']}\n",
            "\n",
            "Rank 4\n",
            "{'id': 'CAND_0000050', 'name': 'Naina Bose', 'title': 'Business Analyst', 'score': 55.59, 'matched': []}\n",
            "\n",
            "Rank 5\n",
            "{'id': 'CAND_0000016', 'name': 'Aanya Malhotra', 'title': 'Accountant', 'score': 53.27, 'matched': ['sql']}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "AI_KEYWORDS = [\n",
        "    \"machine learning\",\n",
        "    \"ml engineer\",\n",
        "    \"ai engineer\",\n",
        "    \"llm\",\n",
        "    \"nlp\",\n",
        "    \"retrieval\",\n",
        "    \"recommendation\",\n",
        "    \"vector\",\n",
        "    \"embedding\",\n",
        "    \"fine-tuning\",\n",
        "    \"mlops\",\n",
        "    \"faiss\",\n",
        "    \"milvus\"\n",
        "]\n",
        "\n",
        "\n",
        "def ai_relevance(candidate):\n",
        "\n",
        "    text = (\n",
        "        candidate[\"profile\"][\"current_title\"] + \" \" +\n",
        "        candidate[\"profile\"][\"summary\"] + \" \" +\n",
        "        \" \".join(\n",
        "            job[\"description\"]\n",
        "            for job in candidate[\"career_history\"]\n",
        "        )\n",
        "    ).lower()\n",
        "\n",
        "    score = sum(\n",
        "        1 for word in AI_KEYWORDS\n",
        "        if word in text\n",
        "    )\n",
        "\n",
        "    return score"
      ],
      "metadata": {
        "id": "Z0ZTp2vL-lC0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(ai_relevance(candidates[0]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VF4R3VQm-3kn",
        "outputId": "11f36b4a-da9e-43da-81d4-0603e1be97d0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def score_candidate(c):\n",
        "\n",
        "    skills = {x[\"name\"].lower() for x in c[\"skills\"]}\n",
        "    required = {x.lower() for x in JOB[\"required_skills\"]}\n",
        "\n",
        "    matched = skills & required\n",
        "    skill_score = len(matched) / len(required) * 100\n",
        "\n",
        "    exp = c[\"profile\"][\"years_of_experience\"]\n",
        "    exp_score = min(exp / 8 * 100, 100)\n",
        "\n",
        "    rr = c[\"redrob_signals\"]\n",
        "\n",
        "    behavior_score = (\n",
        "        rr[\"profile_completeness_score\"] * 0.3 +\n",
        "        rr[\"interview_completion_rate\"] * 30 +\n",
        "        rr[\"github_activity_score\"] * 2 +\n",
        "        rr[\"recruiter_response_rate\"] * 20\n",
        "    )\n",
        "\n",
        "    ai_score = ai_relevance(c) * 10\n",
        "\n",
        "    final_score = (\n",
        "        0.40 * skill_score +\n",
        "        0.25 * exp_score +\n",
        "        0.20 * behavior_score +\n",
        "        0.15 * ai_score\n",
        "    )\n",
        "\n",
        "    return {\n",
        "        \"id\": c[\"candidate_id\"],\n",
        "        \"name\": c[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": c[\"profile\"][\"current_title\"],\n",
        "        \"score\": round(final_score, 2),\n",
        "        \"matched\": list(matched),\n",
        "        \"ai_score\": ai_score\n",
        "    }"
      ],
      "metadata": {
        "id": "ndjMW9qL_G5f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "C2PPSQCIATGq",
        "outputId": "79d0d952-da7f-402a-fe1e-ba17fbf19237"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-ac7e5303-f069-42be-803f-e1cb2e4605c4\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-ac7e5303-f069-42be-803f-e1cb2e4605c4\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving sample_candidates.json to sample_candidates.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "\n",
        "with open(\"sample_candidates.json\", \"r\", encoding=\"utf-8\") as f:\n",
        "    candidates = json.load(f)\n",
        "\n",
        "print(\"Total candidates:\", len(candidates))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AcFzQa3KAg37",
        "outputId": "e0388060-9c16-4d7c-e0a5-8338e1f9bfec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total candidates: 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "JOB = {\n",
        "    \"required_skills\": [\n",
        "        \"Python\",\n",
        "        \"SQL\",\n",
        "        \"Spark\",\n",
        "        \"Machine Learning\",\n",
        "        \"NLP\",\n",
        "        \"Fine-tuning LLMs\",\n",
        "        \"MLOps\",\n",
        "        \"Milvus\",\n",
        "        \"FAISS\"\n",
        "    ]\n",
        "}"
      ],
      "metadata": {
        "id": "ipy8FVNEAswm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "AI_KEYWORDS = [\n",
        "    \"machine learning\",\n",
        "    \"ml engineer\",\n",
        "    \"ai engineer\",\n",
        "    \"llm\",\n",
        "    \"nlp\",\n",
        "    \"retrieval\",\n",
        "    \"recommendation\",\n",
        "    \"vector\",\n",
        "    \"embedding\",\n",
        "    \"fine-tuning\",\n",
        "    \"mlops\",\n",
        "    \"faiss\",\n",
        "    \"milvus\"\n",
        "]"
      ],
      "metadata": {
        "id": "3L9JHSs0AxxH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def ai_relevance(candidate):\n",
        "\n",
        "    text = (\n",
        "        candidate[\"profile\"][\"current_title\"] + \" \" +\n",
        "        candidate[\"profile\"][\"summary\"] + \" \" +\n",
        "        \" \".join(job[\"description\"] for job in candidate[\"career_history\"])\n",
        "    ).lower()\n",
        "\n",
        "    score = sum(\n",
        "        1 for word in AI_KEYWORDS\n",
        "        if word in text\n",
        "    )\n",
        "\n",
        "    return score"
      ],
      "metadata": {
        "id": "mbv5NvoOA3lb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def score_candidate(c):\n",
        "\n",
        "    skills = {x[\"name\"].lower() for x in c[\"skills\"]}\n",
        "    required = {x.lower() for x in JOB[\"required_skills\"]}\n",
        "\n",
        "    matched = skills & required\n",
        "    skill_score = len(matched) / len(required) * 100\n",
        "\n",
        "    exp = c[\"profile\"][\"years_of_experience\"]\n",
        "    exp_score = min(exp / 8 * 100, 100)\n",
        "\n",
        "    rr = c[\"redrob_signals\"]\n",
        "\n",
        "    behavior_score = (\n",
        "        rr[\"profile_completeness_score\"] * 0.3 +\n",
        "        rr[\"interview_completion_rate\"] * 30 +\n",
        "        rr[\"github_activity_score\"] * 2 +\n",
        "        rr[\"recruiter_response_rate\"] * 20\n",
        "    )\n",
        "\n",
        "    ai_score = ai_relevance(c) * 10\n",
        "\n",
        "    final_score = (\n",
        "        0.40 * skill_score +\n",
        "        0.25 * exp_score +\n",
        "        0.20 * behavior_score +\n",
        "        0.15 * ai_score\n",
        "    )\n",
        "\n",
        "    return {\n",
        "        \"id\": c[\"candidate_id\"],\n",
        "        \"name\": c[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": c[\"profile\"][\"current_title\"],\n",
        "        \"score\": round(final_score, 2),\n",
        "        \"matched\": list(matched),\n",
        "        \"ai_score\": ai_score\n",
        "    }"
      ],
      "metadata": {
        "id": "jeAjJKaBA9pr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "results = [score_candidate(c) for c in candidates]\n",
        "results.sort(key=lambda x: x[\"score\"], reverse=True)\n",
        "\n",
        "for i, r in enumerate(results[:5], 1):\n",
        "    print(f\"\\nRank {i}\")\n",
        "    print(r)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jn7zLjKxBrjD",
        "outputId": "fdacde5a-81f3-484f-bbec-6f4834eafdfa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Rank 1\n",
            "{'id': 'CAND_0000031', 'name': 'Ela Singh', 'title': 'Recommendation Systems Engineer', 'score': 66.37, 'matched': ['machine learning', 'mlops', 'faiss'], 'ai_score': 60}\n",
            "\n",
            "Rank 2\n",
            "{'id': 'CAND_0000024', 'name': 'Rajesh Arora', 'title': 'HR Manager', 'score': 54.72, 'matched': [], 'ai_score': 10}\n",
            "\n",
            "Rank 3\n",
            "{'id': 'CAND_0000050', 'name': 'Naina Bose', 'title': 'Business Analyst', 'score': 52.09, 'matched': [], 'ai_score': 10}\n",
            "\n",
            "Rank 4\n",
            "{'id': 'CAND_0000001', 'name': 'Ira Vora', 'title': 'Backend Engineer', 'score': 50.91, 'matched': ['milvus', 'fine-tuning llms', 'nlp'], 'ai_score': 10}\n",
            "\n",
            "Rank 5\n",
            "{'id': 'CAND_0000016', 'name': 'Aanya Malhotra', 'title': 'Accountant', 'score': 48.85, 'matched': ['sql'], 'ai_score': 0}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "NON_AI_ROLES = [\n",
        "    \"hr\",\n",
        "    \"human resources\",\n",
        "    \"accountant\",\n",
        "    \"business analyst\",\n",
        "    \"sales\",\n",
        "    \"marketing\",\n",
        "    \"recruiter\",\n",
        "    \"finance\",\n",
        "    \"customer support\"\n",
        "]\n",
        "\n",
        "def role_penalty(candidate):\n",
        "\n",
        "    title = candidate[\"profile\"][\"current_title\"].lower()\n",
        "\n",
        "    for role in NON_AI_ROLES:\n",
        "        if role in title:\n",
        "            return -30\n",
        "\n",
        "    return 0"
      ],
      "metadata": {
        "id": "EZCGB1eEC8O1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def score_candidate(c):\n",
        "\n",
        "    skills = {x[\"name\"].lower() for x in c[\"skills\"]}\n",
        "    required = {x.lower() for x in JOB[\"required_skills\"]}\n",
        "\n",
        "    matched = skills & required\n",
        "    skill_score = len(matched) / len(required) * 100\n",
        "\n",
        "    exp = c[\"profile\"][\"years_of_experience\"]\n",
        "    exp_score = min(exp / 8 * 100, 100)\n",
        "\n",
        "    rr = c[\"redrob_signals\"]\n",
        "\n",
        "    behavior_score = (\n",
        "        rr[\"profile_completeness_score\"] * 0.3 +\n",
        "        rr[\"interview_completion_rate\"] * 30 +\n",
        "        rr[\"github_activity_score\"] * 2 +\n",
        "        rr[\"recruiter_response_rate\"] * 20\n",
        "    )\n",
        "\n",
        "    ai_score = ai_relevance(c) * 10\n",
        "    penalty = role_penalty(c)\n",
        "\n",
        "    final_score = (\n",
        "        0.45 * skill_score +\n",
        "        0.25 * exp_score +\n",
        "        0.15 * behavior_score +\n",
        "        0.15 * ai_score\n",
        "    ) + penalty\n",
        "\n",
        "    return {\n",
        "        \"id\": c[\"candidate_id\"],\n",
        "        \"name\": c[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": c[\"profile\"][\"current_title\"],\n",
        "        \"score\": round(final_score, 2),\n",
        "        \"matched\": list(matched),\n",
        "        \"ai_score\": ai_score\n",
        "    }"
      ],
      "metadata": {
        "id": "uAowB7MPDEbu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "results = [score_candidate(c) for c in candidates]\n",
        "results.sort(key=lambda x: x[\"score\"], reverse=True)\n",
        "\n",
        "for i, r in enumerate(results[:10], 1):\n",
        "    print(f\"\\nRank {i}\")\n",
        "    print(r)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OVhVRIKmDKtR",
        "outputId": "f4167143-25dd-4996-f385-33d88064ce03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Rank 1\n",
            "{'id': 'CAND_0000031', 'name': 'Ela Singh', 'title': 'Recommendation Systems Engineer', 'score': 61.71, 'matched': ['machine learning', 'mlops', 'faiss'], 'ai_score': 60}\n",
            "\n",
            "Rank 2\n",
            "{'id': 'CAND_0000001', 'name': 'Ira Vora', 'title': 'Backend Engineer', 'score': 48.95, 'matched': ['milvus', 'fine-tuning llms', 'nlp'], 'ai_score': 10}\n",
            "\n",
            "Rank 3\n",
            "{'id': 'CAND_0000021', 'name': 'Rahul Joshi', 'title': 'Project Manager', 'score': 46.41, 'matched': ['fine-tuning llms', 'faiss'], 'ai_score': 20}\n",
            "\n",
            "Rank 4\n",
            "{'id': 'CAND_0000010', 'name': 'Aarav Kapoor', 'title': 'Data Engineer', 'score': 43.24, 'matched': ['python', 'mlops'], 'ai_score': 10}\n",
            "\n",
            "Rank 5\n",
            "{'id': 'CAND_0000038', 'name': 'Myra Trivedi', 'title': 'Java Developer', 'score': 42.86, 'matched': ['mlops'], 'ai_score': 0}\n",
            "\n",
            "Rank 6\n",
            "{'id': 'CAND_0000032', 'name': 'Pranav Agarwal', 'title': '.NET Developer', 'score': 41.87, 'matched': ['python', 'spark'], 'ai_score': 0}\n",
            "\n",
            "Rank 7\n",
            "{'id': 'CAND_0000033', 'name': 'Shreya Nair', 'title': 'Graphic Designer', 'score': 41.72, 'matched': [], 'ai_score': 0}\n",
            "\n",
            "Rank 8\n",
            "{'id': 'CAND_0000041', 'name': 'Anjali Khanna', 'title': 'Operations Manager', 'score': 38.65, 'matched': ['sql'], 'ai_score': 10}\n",
            "\n",
            "Rank 9\n",
            "{'id': 'CAND_0000046', 'name': 'Dev Nair', 'title': 'Mechanical Engineer', 'score': 38.54, 'matched': [], 'ai_score': 10}\n",
            "\n",
            "Rank 10\n",
            "{'id': 'CAND_0000014', 'name': 'Atharv Joshi', 'title': 'Frontend Engineer', 'score': 37.36, 'matched': ['faiss'], 'ai_score': 0}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "GkFR0ISFDsrx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 325
        },
        "id": "ew00nmbBFMRw",
        "outputId": "bd6d9cc4-c76e-4734-b317-ba66c08099b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-6044481f-5956-40f7-a8bd-61d4b289dbd8\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-6044481f-5956-40f7-a8bd-61d4b289dbd8\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_5037/1613494533.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolab\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mfiles\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mfiles\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/files.py\u001b[0m in \u001b[0;36mupload\u001b[0;34m(target_dir)\u001b[0m\n\u001b[1;32m     67\u001b[0m   \"\"\"\n\u001b[1;32m     68\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 69\u001b[0;31m   \u001b[0muploaded_files\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_upload_files\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmultiple\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     70\u001b[0m   \u001b[0;31m# Mapping from original filename to filename as saved locally.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     71\u001b[0m   \u001b[0mlocal_filenames\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/files.py\u001b[0m in \u001b[0;36m_upload_files\u001b[0;34m(multiple)\u001b[0m\n\u001b[1;32m    159\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    160\u001b[0m   \u001b[0;31m# First result is always an indication that the file picker has completed.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 161\u001b[0;31m   result = _output.eval_js(\n\u001b[0m\u001b[1;32m    162\u001b[0m       'google.colab._files._uploadFiles(\"{input_id}\", \"{output_id}\")'.format(\n\u001b[1;32m    163\u001b[0m           \u001b[0minput_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minput_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moutput_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moutput_id\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/output/_js.py\u001b[0m in \u001b[0;36meval_js\u001b[0;34m(script, ignore_result, timeout_sec)\u001b[0m\n\u001b[1;32m     38\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mignore_result\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m     \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 40\u001b[0;31m   \u001b[0;32mreturn\u001b[0m \u001b[0m_message\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_reply_from_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_sec\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     41\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mread_reply_from_input\u001b[0;34m(message_id, timeout_sec)\u001b[0m\n\u001b[1;32m     94\u001b[0m     \u001b[0mreply\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_read_next_input_message\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     95\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mreply\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0m_NOT_READY\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreply\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m       \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0.025\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m       \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     98\u001b[0m     if (\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "XMha09MmJ5cm",
        "outputId": "b461fa97-cdc4-443b-ea14-bec726ab000d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-a402d60d-1d2a-4f8c-9237-a649f390123b\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-a402d60d-1d2a-4f8c-9237-a649f390123b\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving sample_submission.csv to sample_submission.csv\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'sample_submission.csv': b'candidate_id,rank,score,reasoning\\r\\nCAND_0004989,1,0.9920,HR Manager with 6.1 yrs; 9 AI core skills; response rate 0.76.\\r\\nCAND_0001195,2,0.9840,HR Manager with 8.7 yrs; 9 AI core skills; response rate 0.20.\\r\\nCAND_0003114,3,0.9760,ML Engineer with 6.4 yrs; 4 AI core skills; response rate 0.88.\\r\\nCAND_0000339,4,0.9680,Content Writer with 8.3 yrs; 8 AI core skills; response rate 0.72.\\r\\nCAND_0001082,5,0.9600,HR Manager with 5.0 yrs; 8 AI core skills; response rate 0.62.\\r\\nCAND_0001218,6,0.9520,Graphic Designer with 10.4 yrs; 9 AI core skills; response rate 0.56.\\r\\nCAND_0004558,7,0.9440,Business Analyst with 5.1 yrs; 8 AI core skills; response rate 0.54.\\r\\nCAND_0001753,8,0.9360,Content Writer with 8.3 yrs; 8 AI core skills; response rate 0.53.\\r\\nCAND_0001503,9,0.9280,Marketing Manager with 8.0 yrs; 8 AI core skills; response rate 0.32.\\r\\nCAND_0004548,10,0.9200,HR Manager with 7.3 yrs; 8 AI core skills; response rate 0.30.\\r\\nCAND_0002164,11,0.9120,Marketing Manager with 13.2 yrs; 9 AI core skills; response rate 0.24.\\r\\nCAND_0001154,12,0.9040,Mechanical Engineer with 6.9 yrs; 8 AI core skills; response rate 0.18.\\r\\nCAND_0002622,13,0.8960,Accountant with 14.2 yrs; 9 AI core skills; response rate 0.18.\\r\\nCAND_0000002,14,0.8880,Civil Engineer with 8.0 yrs; 8 AI core skills; response rate 0.15.\\r\\nCAND_0000718,15,0.8800,Accountant with 8.2 yrs; 8 AI core skills; response rate 0.15.\\r\\nCAND_0004224,16,0.8720,Graphic Designer with 5.0 yrs; 8 AI core skills; response rate 0.11.\\r\\nCAND_0000239,17,0.8640,Project Manager with 5.0 yrs; 8 AI core skills; response rate 0.10.\\r\\nCAND_0001771,18,0.8560,Accountant with 7.4 yrs; 8 AI core skills; response rate 0.06.\\r\\nCAND_0002782,19,0.8480,Sales Executive with 7.8 yrs; 8 AI core skills; response rate 0.06.\\r\\nCAND_0003693,20,0.8400,Sales Executive with 7.2 yrs; 7 AI core skills; response rate 0.77.\\r\\nCAND_0004937,21,0.8320,Operations Manager with 13.5 yrs; 8 AI core skills; response rate 0.77.\\r\\nCAND_0001397,22,0.8240,Business Analyst with 11.3 yrs; 8 AI core skills; response rate 0.76.\\r\\nCAND_0001381,23,0.8160,Accountant with 14.1 yrs; 8 AI core skills; response rate 0.75.\\r\\nCAND_0004201,24,0.8080,Mechanical Engineer with 13.7 yrs; 8 AI core skills; response rate 0.75.\\r\\nCAND_0002019,25,0.8000,Marketing Manager with 2.0 yrs; 8 AI core skills; response rate 0.73.\\r\\nCAND_0004645,26,0.7920,Project Manager with 10.2 yrs; 8 AI core skills; response rate 0.71.\\r\\nCAND_0004824,27,0.7840,AI Engineer with 6.1 yrs; 3 AI core skills; response rate 0.71.\\r\\nCAND_0002592,28,0.7760,Business Analyst with 11.4 yrs; 8 AI core skills; response rate 0.65.\\r\\nCAND_0001586,29,0.7680,Operations Manager with 6.5 yrs; 7 AI core skills; response rate 0.60.\\r\\nCAND_0001653,30,0.7600,Mechanical Engineer with 4.5 yrs; 8 AI core skills; response rate 0.59.\\r\\nCAND_0000007,31,0.7520,AI Engineer with 6.6 yrs; 3 AI core skills; response rate 0.57.\\r\\nCAND_0001795,32,0.7440,Mechanical Engineer with 4.4 yrs; 8 AI core skills; response rate 0.57.\\r\\nCAND_0003531,33,0.7360,Operations Manager with 3.2 yrs; 8 AI core skills; response rate 0.55.\\r\\nCAND_0002989,34,0.7280,Graphic Designer with 6.0 yrs; 7 AI core skills; response rate 0.54.\\r\\nCAND_0000581,35,0.7200,HR Manager with 8.5 yrs; 7 AI core skills; response rate 0.53.\\r\\nCAND_0004680,36,0.7120,Mechanical Engineer with 8.0 yrs; 7 AI core skills; response rate 0.53.\\r\\nCAND_0001257,37,0.7040,Mechanical Engineer with 6.9 yrs; 7 AI core skills; response rate 0.52.\\r\\nCAND_0002018,38,0.6960,Civil Engineer with 6.4 yrs; 7 AI core skills; response rate 0.52.\\r\\nCAND_0004952,39,0.6880,Project Manager with 6.5 yrs; 7 AI core skills; response rate 0.52.\\r\\nCAND_0001378,40,0.6800,Project Manager with 5.6 yrs; 7 AI core skills; response rate 0.51.\\r\\nCAND_0000164,41,0.6720,Business Analyst with 3.0 yrs; 8 AI core skills; response rate 0.50.\\r\\nCAND_0003406,42,0.6640,Graphic Designer with 6.0 yrs; 7 AI core skills; response rate 0.44.\\r\\nCAND_0000557,43,0.6560,Civil Engineer with 14.3 yrs; 8 AI core skills; response rate 0.43.\\r\\nCAND_0003107,44,0.6480,Customer Support with 6.6 yrs; 7 AI core skills; response rate 0.41.\\r\\nCAND_0000168,45,0.6400,Marketing Manager with 6.3 yrs; 7 AI core skills; response rate 0.39.\\r\\nCAND_0000268,46,0.6320,Accountant with 3.7 yrs; 8 AI core skills; response rate 0.39.\\r\\nCAND_0000791,47,0.6240,Customer Support with 11.5 yrs; 8 AI core skills; response rate 0.39.\\r\\nCAND_0003050,48,0.6160,ML Engineer with 6.0 yrs; 3 AI core skills; response rate 0.38.\\r\\nCAND_0003241,49,0.6080,ML Engineer with 3.6 yrs; 4 AI core skills; response rate 0.36.\\r\\nCAND_0000776,50,0.6000,Operations Manager with 14.2 yrs; 8 AI core skills; response rate 0.35.\\r\\nCAND_0002234,51,0.5920,Content Writer with 9.9 yrs; 8 AI core skills; response rate 0.35.\\r\\nCAND_0004217,52,0.5840,Accountant with 1.8 yrs; 8 AI core skills; response rate 0.33.\\r\\nCAND_0003702,53,0.5760,Graphic Designer with 6.9 yrs; 7 AI core skills; response rate 0.26.\\r\\nCAND_0004154,54,0.5680,HR Manager with 6.2 yrs; 7 AI core skills; response rate 0.26.\\r\\nCAND_0000542,55,0.5600,Mechanical Engineer with 8.5 yrs; 7 AI core skills; response rate 0.25.\\r\\nCAND_0002466,56,0.5520,Marketing Manager with 14.6 yrs; 8 AI core skills; response rate 0.25.\\r\\nCAND_0002974,57,0.5440,Operations Manager with 13.4 yrs; 8 AI core skills; response rate 0.25.\\r\\nCAND_0000450,58,0.5360,Operations Manager with 7.7 yrs; 7 AI core skills; response rate 0.24.\\r\\nCAND_0002438,59,0.5280,Accountant with 1.0 yrs; 8 AI core skills; response rate 0.24.\\r\\nCAND_0000217,60,0.5200,Sales Executive with 11.4 yrs; 8 AI core skills; response rate 0.23.\\r\\nCAND_0001424,61,0.5120,Content Writer with 13.6 yrs; 8 AI core skills; response rate 0.22.\\r\\nCAND_0004711,62,0.5040,Content Writer with 14.2 yrs; 8 AI core skills; response rate 0.22.\\r\\nCAND_0001294,63,0.4960,HR Manager with 3.0 yrs; 8 AI core skills; response rate 0.21.\\r\\nCAND_0001724,64,0.4880,Mechanical Engineer with 7.4 yrs; 7 AI core skills; response rate 0.20.\\r\\nCAND_0002794,65,0.4800,Project Manager with 13.9 yrs; 8 AI core skills; response rate 0.20.\\r\\nCAND_0001292,66,0.4720,Customer Support with 7.6 yrs; 7 AI core skills; response rate 0.16.\\r\\nCAND_0004655,67,0.4640,Mechanical Engineer with 4.4 yrs; 8 AI core skills; response rate 0.16.\\r\\nCAND_0004133,68,0.4560,Sales Executive with 8.5 yrs; 7 AI core skills; response rate 0.14.\\r\\nCAND_0000958,69,0.4480,Business Analyst with 4.3 yrs; 8 AI core skills; response rate 0.13.\\r\\nCAND_0003259,70,0.4400,Project Manager with 5.3 yrs; 7 AI core skills; response rate 0.13.\\r\\nCAND_0004851,71,0.4320,HR Manager with 6.3 yrs; 7 AI core skills; response rate 0.12.\\r\\nCAND_0002626,72,0.4240,Operations Manager with 11.0 yrs; 8 AI core skills; response rate 0.11.\\r\\nCAND_0004410,73,0.4160,Marketing Manager with 11.6 yrs; 8 AI core skills; response rate 0.07.\\r\\nCAND_0003477,74,0.4080,Junior ML Engineer with 6.9 yrs; 2 AI core skills; response rate 0.86.\\r\\nCAND_0000799,75,0.4000,Senior Machine Learning Engineer with 6.3 yrs; 6 AI core skills; response rate 0.83.\\r\\nCAND_0003242,76,0.3920,Project Manager with 13.9 yrs; 7 AI core skills; response rate 0.77.\\r\\nCAND_0003846,77,0.3840,Content Writer with 8.2 yrs; 6 AI core skills; response rate 0.77.\\r\\nCAND_0000459,78,0.3760,HR Manager with 1.9 yrs; 7 AI core skills; response rate 0.76.\\r\\nCAND_0004223,79,0.3680,Civil Engineer with 5.6 yrs; 6 AI core skills; response rate 0.76.\\r\\nCAND_0004640,80,0.3600,Civil Engineer with 11.2 yrs; 7 AI core skills; response rate 0.76.\\r\\nCAND_0000251,81,0.3520,HR Manager with 12.6 yrs; 7 AI core skills; response rate 0.75.\\r\\nCAND_0002255,82,0.3440,Accountant with 3.0 yrs; 7 AI core skills; response rate 0.73.\\r\\nCAND_0003638,83,0.3360,Sales Executive with 13.3 yrs; 7 AI core skills; response rate 0.73.\\r\\nCAND_0003002,84,0.3280,Project Manager with 11.0 yrs; 7 AI core skills; response rate 0.71.\\r\\nCAND_0002880,85,0.3200,Mechanical Engineer with 11.9 yrs; 7 AI core skills; response rate 0.70.\\r\\nCAND_0000084,86,0.3120,Sales Executive with 12.4 yrs; 7 AI core skills; response rate 0.69.\\r\\nCAND_0003300,87,0.3040,Graphic Designer with 6.2 yrs; 6 AI core skills; response rate 0.69.\\r\\nCAND_0000699,88,0.2960,Graphic Designer with 11.7 yrs; 7 AI core skills; response rate 0.68.\\r\\nCAND_0002446,89,0.2880,Customer Support with 10.2 yrs; 7 AI core skills; response rate 0.67.\\r\\nCAND_0003918,90,0.2800,Marketing Manager with 4.3 yrs; 7 AI core skills; response rate 0.66.\\r\\nCAND_0002661,91,0.2720,Graphic Designer with 7.9 yrs; 6 AI core skills; response rate 0.65.\\r\\nCAND_0000899,92,0.2640,Sales Executive with 10.2 yrs; 7 AI core skills; response rate 0.64.\\r\\nCAND_0001550,93,0.2560,Mechanical Engineer with 2.4 yrs; 7 AI core skills; response rate 0.64.\\r\\nCAND_0002317,94,0.2480,Content Writer with 7.2 yrs; 6 AI core skills; response rate 0.62.\\r\\nCAND_0002720,95,0.2400,Civil Engineer with 7.4 yrs; 6 AI core skills; response rate 0.61.\\r\\nCAND_0001355,96,0.2320,Civil Engineer with 12.9 yrs; 7 AI core skills; response rate 0.59.\\r\\nCAND_0001839,97,0.2240,Operations Manager with 8.2 yrs; 6 AI core skills; response rate 0.58.\\r\\nCAND_0004366,98,0.2160,Accountant with 3.6 yrs; 7 AI core skills; response rate 0.58.\\r\\nCAND_0001021,99,0.2080,Data Scientist with 3.1 yrs; 3 AI core skills; response rate 0.57.\\r\\nCAND_0002689,100,0.2000,Content Writer with 14.7 yrs; 7 AI core skills; response rate 0.57.\\r\\n'}"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "-0kP_pRNDfFw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "sub = pd.read_csv(\"sample_submission.csv\")\n",
        "\n",
        "print(sub.head())\n",
        "print(sub.columns)\n",
        "print(sub.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TFU4SysgKxdT",
        "outputId": "8c7c7d74-4b79-430e-b153-9b38db2f016c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   candidate_id  rank  score  \\\n",
            "0  CAND_0004989     1  0.992   \n",
            "1  CAND_0001195     2  0.984   \n",
            "2  CAND_0003114     3  0.976   \n",
            "3  CAND_0000339     4  0.968   \n",
            "4  CAND_0001082     5  0.960   \n",
            "\n",
            "                                           reasoning  \n",
            "0  HR Manager with 6.1 yrs; 9 AI core skills; res...  \n",
            "1  HR Manager with 8.7 yrs; 9 AI core skills; res...  \n",
            "2  ML Engineer with 6.4 yrs; 4 AI core skills; re...  \n",
            "3  Content Writer with 8.3 yrs; 8 AI core skills;...  \n",
            "4  HR Manager with 5.0 yrs; 8 AI core skills; res...  \n",
            "Index(['candidate_id', 'rank', 'score', 'reasoning'], dtype='object')\n",
            "(100, 4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ABY_eJOEKw1A",
        "outputId": "df0658cd-83d8-4b27-a297-3b769bc282fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "job_description.docx\tsample_data\n",
            "sample_candidates.json\tsample_submission.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install python-docx"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "awZ3wlUPMVAF",
        "outputId": "19211b85-c037-468a-e878-717c7879da9b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting python-docx\n",
            "  Downloading python_docx-1.2.0-py3-none-any.whl.metadata (2.0 kB)\n",
            "Requirement already satisfied: lxml>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (6.1.1)\n",
            "Requirement already satisfied: typing_extensions>=4.9.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (4.15.0)\n",
            "Downloading python_docx-1.2.0-py3-none-any.whl (252 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m253.0/253.0 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: python-docx\n",
            "Successfully installed python-docx-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from docx import Document\n",
        "\n",
        "doc = Document(\"job_description.docx\")\n",
        "\n",
        "text = \"\"\n",
        "\n",
        "for para in doc.paragraphs:\n",
        "    text += para.text + \"\\n\"\n",
        "\n",
        "print(text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "341CInhJMZHX",
        "outputId": "1c82c5d6-53fc-425a-8955-b36ae1894c22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Job Description: Senior AI Engineer — Founding Team\n",
            "Company: Redrob AI (Series A AI-native talent intelligence platform)\n",
            "Location: Pune/Noida, India (Hybrid — flexible cadence) | Open to relocation candidates from Tier-1 Indian cities\n",
            "Employment Type: Full-time\n",
            "Experience Required: 5–9 years (see \"what we mean by this\" below)\n",
            "\n",
            "Let's be honest about this role\n",
            "We're going to write this JD differently from most. We're a Series A company that just raised our round and we're building a new AI Engineering org from scratch. This is the kind of role where the JD changes every six months because the company changes every six months. So instead of pretending we have a fixed checklist, we're going to tell you what we actually need and what we've gotten wrong before.\n",
            "If you've spent your career at Google or Meta and you want a well-scoped role with a defined ladder, this isn't it.\n",
            "If you've spent your career bouncing between early-stage startups and you want to \"just code\" without having to think about product or recruiter workflows or eval frameworks, this also isn't it.\n",
            "We need someone who is simultaneously comfortable with two things that sound contradictory:\n",
            "Deep technical depth in modern ML systems — embeddings, retrieval, ranking, LLMs, fine-tuning.\n",
            "Scrappy product-engineering attitude — willing to ship a working ranker in a week even if the underlying ML is \"obviously suboptimal,\" because we need to learn from real users before we know what to actually optimize for.\n",
            "These are not contradictory in real life. They feel contradictory because of how engineering culture sorted itself into \"researcher\" vs \"shipper\" archetypes. We need both modes available in the same person, and we'd rather you tilt slightly toward shipper than toward researcher.\n",
            "\n",
            "What you'd actually be doing\n",
            "The high-level mandate: own the intelligence layer of Redrob's product. That means the ranking, retrieval, and matching systems that decide what recruiters see when they search for candidates and what candidates see when they search for roles.\n",
            "In practical terms, your first 90 days will probably look like:\n",
            "Weeks 1-3: Audit what we currently have (it's mostly BM25 + rule-based scoring, working but not great). Identify the 3-4 highest-leverage things to fix.\n",
            "Weeks 4-8: Ship a v2 ranking system that demonstrably improves recruiter-engagement metrics. This will involve embeddings, hybrid retrieval, and probably some LLM-based re-ranking, but the architecture is your call.\n",
            "Weeks 9-12: Set up the evaluation infrastructure — offline benchmarks, online A/B testing, recruiter-feedback loops — so we can keep improving without flying blind.\n",
            "Beyond that, you'll be driving the long-term architecture of how we do candidate-JD matching at scale, mentoring the next round of hires (we're growing the team from 4 to 12 engineers in the next year), and working closely with our recruiter-experience PM on what to build.\n",
            "\n",
            "What we mean by \"5-9 years\"\n",
            "This is a range, not a requirement. Some people hit \"senior engineer\" judgment at 4 years; some never hit it after 15. We've used 5-9 because it's roughly where people we've hired into this kind of role have landed, but we'll seriously consider candidates outside the band if other signals are strong.\n",
            "That said, here are the disqualifiers we actually apply:\n",
            "If you've spent your career in pure research environments (academic labs, research-only roles) without any production deployment — we will not move forward. We are explicit about this. We've tried it twice and it didn't work for either side.\n",
            "If your \"AI experience\" consists primarily of recent (under 12 months) projects using LangChain to call OpenAI — we will probably not move forward, unless you can demonstrate substantial pre-LLM-era ML production experience. We're looking for people who understood retrieval and ranking before it became fashionable.\n",
            "If you are a senior engineer who hasn't written production code in the last 18 months because you've moved into \"architecture\" or \"tech lead\" roles — we will probably not move forward. This role writes code.\n",
            "\n",
            "The skills inventory (please read carefully)\n",
            "Most JDs list 20 skills and you're supposed to have all of them. We're going to do this differently.\n",
            "Things you absolutely need\n",
            "Production experience with embeddings-based retrieval systems (sentence-transformers, OpenAI embeddings, BGE, E5, or similar) deployed to real users. We don't care which model — we care that you've handled embedding drift, index refresh, retrieval-quality regression in production.\n",
            "Production experience with vector databases or hybrid search infrastructure — Pinecone, Weaviate, Qdrant, Milvus, OpenSearch, Elasticsearch, FAISS, or something similar. Again, the specific tech doesn't matter; the operational experience does.\n",
            "Strong Python. Yes really, we care about code quality.\n",
            "Hands-on experience designing evaluation frameworks for ranking systems — NDCG, MRR, MAP, offline-to-online correlation, A/B test interpretation. If you've never thought about how to evaluate a ranking system rigorously, this role will be very painful.\n",
            "Things we'd like you to have but won't reject you for\n",
            "LLM fine-tuning experience (LoRA, QLoRA, PEFT)\n",
            "Experience with learning-to-rank models (XGBoost-based or neural)\n",
            "Prior exposure to HR-tech, recruiting tech, or marketplace products\n",
            "Background in distributed systems or large-scale inference optimization\n",
            "Open-source contributions in the AI/ML space\n",
            "Things we explicitly do NOT want\n",
            "This is the section most JDs skip but we think it's the most important:\n",
            "Title-chasers. If your career trajectory shows you optimizing for \"Senior\" → \"Staff\" → \"Principal\" titles by switching companies every 1.5 years, we're not a fit. We need someone who plans to be here for 3+ years.\n",
            "Framework enthusiasts. If your GitHub is full of LangChain tutorials and your blog posts are \"How I used [hot framework] to build [demo]\" — that's fine but it's not what we need. We need people who think about systems, not frameworks.\n",
            "People who have only worked at consulting firms (TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini, etc.) in their entire career. We've had bad fit experiences in both directions. If you're currently at one of these companies but have prior product-company experience, that's fine.\n",
            "People whose primary expertise is computer vision, speech, or robotics without significant NLP/IR exposure. We respect your work but you'd be re-learning fundamentals here.\n",
            "People whose work has been entirely on closed-source proprietary systems for 5+ years without external validation (papers, talks, open-source). We need to see how you think, not just trust that you can think.\n",
            "\n",
            "On location, comp, and logistics\n",
            "Location: Pune/Noida-preferred but flexible. We have offices in Noida and Pune(mostly used Tue/Thu). We don't require any specific number of in-office days but we expect quarterly travel for offsites. Candidates in Hyderabad, Pune, Mumbai, Delhi NCR welcome to apply. Outside India: case-by-case, but we don't sponsor work visas.\n",
            "Notice period: We'd love sub-30-day notice. We can buy out up to 30 days. 30+ day notice candidates are still in scope but the bar gets higher.\n",
            "\n",
            "The vibe check\n",
            "We genuinely believe culture-fit matters more at this stage than skills-fit. Skills are teachable; the rest mostly isn't.\n",
            "We work async-first and write a lot. If you find writing painful, you'll find this role painful.\n",
            "We disagree openly and decide quickly. If you find that style abrasive, you'll find this role abrasive.\n",
            "We move fast and break things, with the caveat that \"things\" are usually our internal assumptions, not user-facing systems. If you need a stable, mature codebase to be productive, you'll find this role unstable.\n",
            "\n",
            "How to read between the lines\n",
            "The \"ideal candidate\" we're imagining is roughly:\n",
            "6-8 years total experience, of which 4-5 are in applied ML/AI roles at product companies (not pure services).\n",
            "Has shipped at least one end-to-end ranking, search, or recommendation system to real users at meaningful scale.\n",
            "Has strong opinions about retrieval (hybrid vs dense), evaluation (offline vs online), and LLM integration (when to fine-tune vs prompt) — and can defend them with reference to systems they actually built.\n",
            "Located in or willing to relocate to Noida or Pune.\n",
            "Active on Redrob platform (or has clear signal of being in the job market) so we can actually talk to them.\n",
            "We are aware this is a narrow profile. We're not expecting to find many matches in a 100K candidate pool. We're explicitly OK with that — we'd rather see 10 great matches than 1000 maybes.\n",
            "\n",
            "Final note for the participants of the Redrob hackathon\n",
            "If you're reading this in the context of the Intelligent Candidate Discovery & Ranking Challenge:\n",
            "The \"right answer\" to this JD is not \"find candidates whose skills section contains the most AI keywords.\" That's a trap we've explicitly built into the dataset.\n",
            "The right answer involves reasoning about the gap between what the JD says and what the JD means. A Tier 5 candidate may not use the words \"RAG\" or \"Pinecone\" in their profile, but if their career history shows they built a recommendation system at a product company, they're a fit. A candidate who has all the AI keywords listed as skills but whose title is \"Marketing Manager\" is not a fit, no matter how perfect their skill list looks.\n",
            "Your ranking system should also weigh behavioral signals — a perfect-on-paper candidate who hasn't logged in for 6 months and has a 5% recruiter response rate is, for hiring purposes, not actually available. Down-weight them appropriately.\n",
            "Good luck.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "CORE_AI_SKILLS = [\n",
        "    \"python\",\n",
        "    \"faiss\",\n",
        "    \"milvus\",\n",
        "    \"pinecone\",\n",
        "    \"weaviate\",\n",
        "    \"qdrant\",\n",
        "    \"machine learning\",\n",
        "    \"nlp\",\n",
        "    \"embeddings\",\n",
        "    \"retrieval\",\n",
        "    \"ranking\",\n",
        "    \"recommendation systems\",\n",
        "    \"fine-tuning llms\",\n",
        "    \"lora\",\n",
        "    \"qlora\",\n",
        "    \"peft\",\n",
        "    \"mlops\"\n",
        "]"
      ],
      "metadata": {
        "id": "Okr6p0OnM2hM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "NON_AI_ROLES = [\n",
        "    \"hr\",\n",
        "    \"marketing\",\n",
        "    \"accountant\",\n",
        "    \"graphic designer\",\n",
        "    \"sales\",\n",
        "    \"customer support\"\n",
        "]"
      ],
      "metadata": {
        "id": "XcG7LtudM4dT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def role_penalty(candidate):\n",
        "\n",
        "    title = candidate[\"profile\"][\"current_title\"].lower()\n",
        "\n",
        "    for role in NON_AI_ROLES:\n",
        "        if role in title:\n",
        "            return -50\n",
        "\n",
        "    return 0"
      ],
      "metadata": {
        "id": "vuWrKCIWM8zi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def experience_bonus(candidate):\n",
        "\n",
        "    exp = candidate[\"profile\"][\"years_of_experience\"]\n",
        "\n",
        "    if 5 <= exp <= 9:\n",
        "        return 20\n",
        "\n",
        "    elif 4 <= exp <= 10:\n",
        "        return 10\n",
        "\n",
        "    return 0"
      ],
      "metadata": {
        "id": "Cv4AZ45kNAPR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def score_candidate(candidate):\n",
        "\n",
        "    skills = [\n",
        "        s[\"name\"].lower()\n",
        "        for s in candidate[\"skills\"]\n",
        "    ]\n",
        "\n",
        "    matched = [\n",
        "        s for s in skills\n",
        "        if s in CORE_AI_SKILLS\n",
        "    ]\n",
        "\n",
        "    ai_score = len(matched) * 10\n",
        "\n",
        "    final_score = (\n",
        "        ai_score\n",
        "        + experience_bonus(candidate)\n",
        "        + role_penalty(candidate)\n",
        "    )\n",
        "\n",
        "    return {\n",
        "        \"id\": candidate[\"candidate_id\"],\n",
        "        \"name\": candidate[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": candidate[\"profile\"][\"current_title\"],\n",
        "        \"score\": final_score,\n",
        "        \"matched\": matched[:5],\n",
        "        \"ai_score\": ai_score\n",
        "    }"
      ],
      "metadata": {
        "id": "L8EKjYDENS5f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "results = [score_candidate(c) for c in candidates]\n",
        "\n",
        "results.sort(\n",
        "    key=lambda x: x[\"score\"],\n",
        "    reverse=True\n",
        ")\n",
        "\n",
        "for i, r in enumerate(results[:10], 1):\n",
        "    print(f\"\\nRank {i}\")\n",
        "    print(r)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CeN_MSe2NVL-",
        "outputId": "b57cdb6a-2e28-43c5-c0cd-5081f81f7e9b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Rank 1\n",
            "{'id': 'CAND_0000031', 'name': 'Ela Singh', 'title': 'Recommendation Systems Engineer', 'score': 70, 'matched': ['faiss', 'pinecone', 'machine learning', 'mlops', 'embeddings'], 'ai_score': 50}\n",
            "\n",
            "Rank 2\n",
            "{'id': 'CAND_0000001', 'name': 'Ira Vora', 'title': 'Backend Engineer', 'score': 60, 'matched': ['nlp', 'fine-tuning llms', 'lora', 'milvus'], 'ai_score': 40}\n",
            "\n",
            "Rank 3\n",
            "{'id': 'CAND_0000021', 'name': 'Rahul Joshi', 'title': 'Project Manager', 'score': 50, 'matched': ['recommendation systems', 'fine-tuning llms', 'pinecone', 'embeddings', 'faiss'], 'ai_score': 50}\n",
            "\n",
            "Rank 4\n",
            "{'id': 'CAND_0000032', 'name': 'Pranav Agarwal', 'title': '.NET Developer', 'score': 40, 'matched': ['embeddings', 'python'], 'ai_score': 20}\n",
            "\n",
            "Rank 5\n",
            "{'id': 'CAND_0000038', 'name': 'Myra Trivedi', 'title': 'Java Developer', 'score': 40, 'matched': ['weaviate', 'mlops'], 'ai_score': 20}\n",
            "\n",
            "Rank 6\n",
            "{'id': 'CAND_0000043', 'name': 'Aarav Sen', 'title': 'Cloud Engineer', 'score': 40, 'matched': ['fine-tuning llms', 'peft'], 'ai_score': 20}\n",
            "\n",
            "Rank 7\n",
            "{'id': 'CAND_0000010', 'name': 'Aarav Kapoor', 'title': 'Data Engineer', 'score': 30, 'matched': ['mlops', 'python'], 'ai_score': 20}\n",
            "\n",
            "Rank 8\n",
            "{'id': 'CAND_0000014', 'name': 'Atharv Joshi', 'title': 'Frontend Engineer', 'score': 30, 'matched': ['faiss'], 'ai_score': 10}\n",
            "\n",
            "Rank 9\n",
            "{'id': 'CAND_0000015', 'name': 'Rahul Agarwal', 'title': 'Software Engineer', 'score': 30, 'matched': ['qdrant'], 'ai_score': 10}\n",
            "\n",
            "Rank 10\n",
            "{'id': 'CAND_0000044', 'name': 'Vihaan Naidu', 'title': 'Frontend Engineer', 'score': 30, 'matched': ['python'], 'ai_score': 10}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "NON_AI_ROLES = [\n",
        "    \"hr\",\n",
        "    \"marketing\",\n",
        "    \"accountant\",\n",
        "    \"graphic designer\",\n",
        "    \"sales\",\n",
        "    \"customer support\",\n",
        "    \"project manager\",\n",
        "    \"frontend engineer\"\n",
        "]"
      ],
      "metadata": {
        "id": "mfqOxO0-NsEv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def title_bonus(candidate):\n",
        "\n",
        "    title = candidate[\"profile\"][\"current_title\"].lower()\n",
        "\n",
        "    good_titles = [\n",
        "        \"ai engineer\",\n",
        "        \"ml engineer\",\n",
        "        \"machine learning engineer\",\n",
        "        \"recommendation systems engineer\",\n",
        "        \"data scientist\"\n",
        "    ]\n",
        "\n",
        "    for t in good_titles:\n",
        "        if t in title:\n",
        "            return 20\n",
        "\n",
        "    return 0"
      ],
      "metadata": {
        "id": "A4PKr0b9Nuye"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def score_candidate(candidate):\n",
        "\n",
        "    skills = [\n",
        "        s[\"name\"].lower()\n",
        "        for s in candidate[\"skills\"]\n",
        "    ]\n",
        "\n",
        "    matched = [\n",
        "        s for s in skills\n",
        "        if s in CORE_AI_SKILLS\n",
        "    ]\n",
        "\n",
        "    ai_score = len(matched) * 10\n",
        "\n",
        "    final_score = (\n",
        "        ai_score\n",
        "        + experience_bonus(candidate)\n",
        "        + role_penalty(candidate)\n",
        "        + title_bonus(candidate)\n",
        "    )\n",
        "\n",
        "    return {\n",
        "        \"id\": candidate[\"candidate_id\"],\n",
        "        \"name\": candidate[\"profile\"][\"anonymized_name\"],\n",
        "        \"title\": candidate[\"profile\"][\"current_title\"],\n",
        "        \"score\": final_score,\n",
        "        \"matched\": matched[:5],\n",
        "        \"ai_score\": ai_score\n",
        "    }"
      ],
      "metadata": {
        "id": "Q04utc5nNwKS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "results = [score_candidate(c) for c in candidates]\n",
        "\n",
        "results.sort(\n",
        "    key=lambda x: x[\"score\"],\n",
        "    reverse=True\n",
        ")\n",
        "\n",
        "for i, r in enumerate(results[:10], 1):\n",
        "    print(f\"\\nRank {i}\")\n",
        "    print(r)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zRIT_ZaIN6E2",
        "outputId": "63c4276b-b453-46e1-ccd9-8416e1154207"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Rank 1\n",
            "{'id': 'CAND_0000031', 'name': 'Ela Singh', 'title': 'Recommendation Systems Engineer', 'score': 90, 'matched': ['faiss', 'pinecone', 'machine learning', 'mlops', 'embeddings'], 'ai_score': 50}\n",
            "\n",
            "Rank 2\n",
            "{'id': 'CAND_0000001', 'name': 'Ira Vora', 'title': 'Backend Engineer', 'score': 60, 'matched': ['nlp', 'fine-tuning llms', 'lora', 'milvus'], 'ai_score': 40}\n",
            "\n",
            "Rank 3\n",
            "{'id': 'CAND_0000032', 'name': 'Pranav Agarwal', 'title': '.NET Developer', 'score': 40, 'matched': ['embeddings', 'python'], 'ai_score': 20}\n",
            "\n",
            "Rank 4\n",
            "{'id': 'CAND_0000038', 'name': 'Myra Trivedi', 'title': 'Java Developer', 'score': 40, 'matched': ['weaviate', 'mlops'], 'ai_score': 20}\n",
            "\n",
            "Rank 5\n",
            "{'id': 'CAND_0000043', 'name': 'Aarav Sen', 'title': 'Cloud Engineer', 'score': 40, 'matched': ['fine-tuning llms', 'peft'], 'ai_score': 20}\n",
            "\n",
            "Rank 6\n",
            "{'id': 'CAND_0000010', 'name': 'Aarav Kapoor', 'title': 'Data Engineer', 'score': 30, 'matched': ['mlops', 'python'], 'ai_score': 20}\n",
            "\n",
            "Rank 7\n",
            "{'id': 'CAND_0000015', 'name': 'Rahul Agarwal', 'title': 'Software Engineer', 'score': 30, 'matched': ['qdrant'], 'ai_score': 10}\n",
            "\n",
            "Rank 8\n",
            "{'id': 'CAND_0000006', 'name': 'Rajesh Desai', 'title': 'Business Analyst', 'score': 20, 'matched': [], 'ai_score': 0}\n",
            "\n",
            "Rank 9\n",
            "{'id': 'CAND_0000007', 'name': 'Vihaan Bose', 'title': 'Civil Engineer', 'score': 20, 'matched': [], 'ai_score': 0}\n",
            "\n",
            "Rank 10\n",
            "{'id': 'CAND_0000020', 'name': 'Aditya Iyengar', 'title': 'Mechanical Engineer', 'score': 20, 'matched': [], 'ai_score': 0}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "submission = pd.DataFrame(results)\n",
        "\n",
        "submission.head(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "bTz6schlODLz",
        "outputId": "7a7f0099-77b7-462b-b06a-16903788a4e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             id            name                            title  score  \\\n",
              "0  CAND_0000031       Ela Singh  Recommendation Systems Engineer     90   \n",
              "1  CAND_0000001        Ira Vora                 Backend Engineer     60   \n",
              "2  CAND_0000032  Pranav Agarwal                   .NET Developer     40   \n",
              "3  CAND_0000038    Myra Trivedi                   Java Developer     40   \n",
              "4  CAND_0000043       Aarav Sen                   Cloud Engineer     40   \n",
              "5  CAND_0000010    Aarav Kapoor                    Data Engineer     30   \n",
              "6  CAND_0000015   Rahul Agarwal                Software Engineer     30   \n",
              "7  CAND_0000006    Rajesh Desai                 Business Analyst     20   \n",
              "8  CAND_0000007     Vihaan Bose                   Civil Engineer     20   \n",
              "9  CAND_0000020  Aditya Iyengar              Mechanical Engineer     20   \n",
              "\n",
              "                                             matched  ai_score  \n",
              "0  [faiss, pinecone, machine learning, mlops, emb...        50  \n",
              "1              [nlp, fine-tuning llms, lora, milvus]        40  \n",
              "2                               [embeddings, python]        20  \n",
              "3                                  [weaviate, mlops]        20  \n",
              "4                           [fine-tuning llms, peft]        20  \n",
              "5                                    [mlops, python]        20  \n",
              "6                                           [qdrant]        10  \n",
              "7                                                 []         0  \n",
              "8                                                 []         0  \n",
              "9                                                 []         0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1aff05d7-0422-47af-96b8-841a80de05cb\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>name</th>\n",
              "      <th>title</th>\n",
              "      <th>score</th>\n",
              "      <th>matched</th>\n",
              "      <th>ai_score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>CAND_0000031</td>\n",
              "      <td>Ela Singh</td>\n",
              "      <td>Recommendation Systems Engineer</td>\n",
              "      <td>90</td>\n",
              "      <td>[faiss, pinecone, machine learning, mlops, emb...</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>CAND_0000001</td>\n",
              "      <td>Ira Vora</td>\n",
              "      <td>Backend Engineer</td>\n",
              "      <td>60</td>\n",
              "      <td>[nlp, fine-tuning llms, lora, milvus]</td>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>CAND_0000032</td>\n",
              "      <td>Pranav Agarwal</td>\n",
              "      <td>.NET Developer</td>\n",
              "      <td>40</td>\n",
              "      <td>[embeddings, python]</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>CAND_0000038</td>\n",
              "      <td>Myra Trivedi</td>\n",
              "      <td>Java Developer</td>\n",
              "      <td>40</td>\n",
              "      <td>[weaviate, mlops]</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>CAND_0000043</td>\n",
              "      <td>Aarav Sen</td>\n",
              "      <td>Cloud Engineer</td>\n",
              "      <td>40</td>\n",
              "      <td>[fine-tuning llms, peft]</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>CAND_0000010</td>\n",
              "      <td>Aarav Kapoor</td>\n",
              "      <td>Data Engineer</td>\n",
              "      <td>30</td>\n",
              "      <td>[mlops, python]</td>\n",
              "      <td>20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>CAND_0000015</td>\n",
              "      <td>Rahul Agarwal</td>\n",
              "      <td>Software Engineer</td>\n",
              "      <td>30</td>\n",
              "      <td>[qdrant]</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>CAND_0000006</td>\n",
              "      <td>Rajesh Desai</td>\n",
              "      <td>Business Analyst</td>\n",
              "      <td>20</td>\n",
              "      <td>[]</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>CAND_0000007</td>\n",
              "      <td>Vihaan Bose</td>\n",
              "      <td>Civil Engineer</td>\n",
              "      <td>20</td>\n",
              "      <td>[]</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>CAND_0000020</td>\n",
              "      <td>Aditya Iyengar</td>\n",
              "      <td>Mechanical Engineer</td>\n",
              "      <td>20</td>\n",
              "      <td>[]</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1aff05d7-0422-47af-96b8-841a80de05cb')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-1aff05d7-0422-47af-96b8-841a80de05cb button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-1aff05d7-0422-47af-96b8-841a80de05cb');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "submission",
              "summary": "{\n  \"name\": \"submission\",\n  \"rows\": 50,\n  \"fields\": [\n    {\n      \"column\": \"id\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 50,\n        \"samples\": [\n          \"CAND_0000011\",\n          \"CAND_0000042\",\n          \"CAND_0000014\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 49,\n        \"samples\": [\n          \"Deepak Desai\",\n          \"Sai Saxena\",\n          \"Vikram Mittal\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"title\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 22,\n        \"samples\": [\n          \"Recommendation Systems Engineer\",\n          \"Mobile Developer\",\n          \"Civil Engineer\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": -50,\n        \"max\": 90,\n        \"num_unique_values\": 11,\n        \"samples\": [\n          10,\n          90,\n          -40\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"matched\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"ai_score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 0,\n        \"max\": 50,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          40,\n          0,\n          20\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "39Ko1jVMOXUQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "submission.to_csv(\n",
        "    \"my_submission.csv\",\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"Submission saved successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iscANMbwOV4s",
        "outputId": "4c949e64-af2c-423c-8cc0-92a070116670"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Submission saved successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YG1rK9rLOjtJ",
        "outputId": "5169ae80-7366-40f3-c4b3-c5f55acb4d55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "job_description.docx  sample_candidates.json  sample_submission.csv\n",
            "my_submission.csv     sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv(\"my_submission.csv\")\n",
        "\n",
        "print(df.head(10))\n",
        "print(df.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CLhCQmFuO2Ib",
        "outputId": "914dc738-f74a-46fa-dabd-b7593c8b9510"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             id            name                            title  score  \\\n",
            "0  CAND_0000031       Ela Singh  Recommendation Systems Engineer     90   \n",
            "1  CAND_0000001        Ira Vora                 Backend Engineer     60   \n",
            "2  CAND_0000032  Pranav Agarwal                   .NET Developer     40   \n",
            "3  CAND_0000038    Myra Trivedi                   Java Developer     40   \n",
            "4  CAND_0000043       Aarav Sen                   Cloud Engineer     40   \n",
            "5  CAND_0000010    Aarav Kapoor                    Data Engineer     30   \n",
            "6  CAND_0000015   Rahul Agarwal                Software Engineer     30   \n",
            "7  CAND_0000006    Rajesh Desai                 Business Analyst     20   \n",
            "8  CAND_0000007     Vihaan Bose                   Civil Engineer     20   \n",
            "9  CAND_0000020  Aditya Iyengar              Mechanical Engineer     20   \n",
            "\n",
            "                                             matched  ai_score  \n",
            "0  ['faiss', 'pinecone', 'machine learning', 'mlo...        50  \n",
            "1      ['nlp', 'fine-tuning llms', 'lora', 'milvus']        40  \n",
            "2                           ['embeddings', 'python']        20  \n",
            "3                              ['weaviate', 'mlops']        20  \n",
            "4                       ['fine-tuning llms', 'peft']        20  \n",
            "5                                ['mlops', 'python']        20  \n",
            "6                                         ['qdrant']        10  \n",
            "7                                                 []         0  \n",
            "8                                                 []         0  \n",
            "9                                                 []         0  \n",
            "(50, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.sort_values(\"score\", ascending=False)\n",
        "print(df.head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XWZzIw8vPYUR",
        "outputId": "a7f79ba0-46fb-4f47-95a4-714e9c8d0e08"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             id            name                            title  score  \\\n",
            "0  CAND_0000031       Ela Singh  Recommendation Systems Engineer     90   \n",
            "1  CAND_0000001        Ira Vora                 Backend Engineer     60   \n",
            "2  CAND_0000032  Pranav Agarwal                   .NET Developer     40   \n",
            "3  CAND_0000038    Myra Trivedi                   Java Developer     40   \n",
            "4  CAND_0000043       Aarav Sen                   Cloud Engineer     40   \n",
            "5  CAND_0000010    Aarav Kapoor                    Data Engineer     30   \n",
            "6  CAND_0000015   Rahul Agarwal                Software Engineer     30   \n",
            "7  CAND_0000006    Rajesh Desai                 Business Analyst     20   \n",
            "8  CAND_0000007     Vihaan Bose                   Civil Engineer     20   \n",
            "9  CAND_0000020  Aditya Iyengar              Mechanical Engineer     20   \n",
            "\n",
            "                                             matched  ai_score  \n",
            "0  ['faiss', 'pinecone', 'machine learning', 'mlo...        50  \n",
            "1      ['nlp', 'fine-tuning llms', 'lora', 'milvus']        40  \n",
            "2                           ['embeddings', 'python']        20  \n",
            "3                              ['weaviate', 'mlops']        20  \n",
            "4                       ['fine-tuning llms', 'peft']        20  \n",
            "5                                ['mlops', 'python']        20  \n",
            "6                                         ['qdrant']        10  \n",
            "7                                                 []         0  \n",
            "8                                                 []         0  \n",
            "9                                                 []         0  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.to_csv(\"final_rankings.csv\", index=False)\n",
        "print(\"Final file saved!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X_pBXoWpPqOy",
        "outputId": "44806e35-0739-489b-e5e9-b68ef93e9318"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Final file saved!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"score\"] = df.apply(\n",
        "    lambda x: x[\"score\"] - 10 if len(x[\"matched\"]) == 0 else x[\"score\"],\n",
        "    axis=1\n",
        ")"
      ],
      "metadata": {
        "id": "E6fyoAzFPwCs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"reason\"] = df[\"matched\"].apply(\n",
        "    lambda x: \"Strong match\" if len(x) >= 3 else \"Weak match\"\n",
        ")"
      ],
      "metadata": {
        "id": "MDElfKtVPxXY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "top = df.head(10)\n",
        "\n",
        "plt.bar(top[\"name\"], top[\"score\"])\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 503
        },
        "id": "TgwpctUXP2GQ",
        "outputId": "6ca05005-17d2-49b0-d27e-9a384876eb94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAHmCAYAAADTKOydAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAbN1JREFUeJzt3XVYVNnjBvBzFQQUAUUFDEQBA0FQEMFAsRUT7O7uAuyu3bUDbOwWu1vX1jXXbhFsEZR+f3/wm/udEXTVhTuD+36eh2fXO5eZw8ydc9977gkJAAQRERGRQjJpuwBERET038LwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKUpP2wX4UlJSkggLCxPZs2cXkiRpuzhERET0HQCIjx8/irx584pMmb7dtqFz4SMsLEwUKFBA28UgIiKin/D06VORP3/+b+6jc+Eje/bsQojkwpuYmGi5NERERPQ9IiMjRYECBeTz+LfoXPhQ3WoxMTFh+CAiIspgvqfLBDucEhERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFKWn7QIozSZgl7aLkMKjKT7aLgIREZFi2PJBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJF/VD4SExMFCNHjhSFChUSRkZGwtbWVowfP14AkPcBIEaNGiWsrKyEkZGRqFatmrh7926aF5yIiIgyph8KH1OnThULFiwQc+fOFX///beYOnWqmDZtmpgzZ468z7Rp08Ts2bNFUFCQOHv2rMiWLZuoWbOmiImJSfPCExERUcaj9yM7//nnn6JBgwbCx8dHCCGEjY2NWLt2rTh37pwQIrnVY+bMmWLEiBGiQYMGQgghVqxYISwsLERoaKho3rx5GhefiIiIMpofavkoV66cOHTokLhz544QQogrV66IkydPitq1awshhHj48KEIDw8X1apVk3/H1NRUlC1bVpw+fTrV54yNjRWRkZEaP0RERPTr+qGWj4CAABEZGSmKFSsmMmfOLBITE8XEiRNFq1athBBChIeHCyGEsLCw0Pg9CwsL+bEvTZ48WYwdO/Znyk5EREQZ0A+1fGzYsEGsXr1arFmzRly6dEmEhISI33//XYSEhPx0AQIDA8WHDx/kn6dPn/70cxEREZHu+6GWjyFDhoiAgAC574aTk5N4/PixmDx5smjXrp2wtLQUQggREREhrKys5N+LiIgQLi4uqT6ngYGBMDAw+MniExERUUbzQy0fnz59Epkyaf5K5syZRVJSkhBCiEKFCglLS0tx6NAh+fHIyEhx9uxZ4enpmQbFJSIioozuh1o+6tWrJyZOnCisra1FiRIlxOXLl8X06dNFx44dhRBCSJIk+vfvLyZMmCDs7e1FoUKFxMiRI0XevHlFw4YN06P8RERElMH8UPiYM2eOGDlypOjZs6d4+fKlyJs3r+jWrZsYNWqUvM/QoUNFdHS06Nq1q3j//r2oUKGC2Lt3rzA0NEzzwhMREVHGI0F9elIdEBkZKUxNTcWHDx+EiYlJmj+/TcCuNH/Of+vRFB9tF4GIiOhf+ZHzN9d2ISIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRPxw+nj9/Llq3bi3Mzc2FkZGRcHJyEhcuXJAfByBGjRolrKyshJGRkahWrZq4e/dumhaaiIiIMq4fCh/v3r0T5cuXF/r6+mLPnj3i5s2b4o8//hA5cuSQ95k2bZqYPXu2CAoKEmfPnhXZsmUTNWvWFDExMWleeCIiIsp49H5k56lTp4oCBQqIZcuWydsKFSok/z8AMXPmTDFixAjRoEEDIYQQK1asEBYWFiI0NFQ0b948jYpNREREGdUPtXxs375duLm5iSZNmog8efKIUqVKiUWLFsmPP3z4UISHh4tq1arJ20xNTUXZsmXF6dOn067URERElGH9UPh48OCBWLBggbC3txf79u0TPXr0EH379hUhISFCCCHCw8OFEEJYWFho/J6FhYX82JdiY2NFZGSkxg8RERH9un7otktSUpJwc3MTkyZNEkIIUapUKXH9+nURFBQk2rVr91MFmDx5shg7duxP/e5/iU3ALm0XIYVHU3y0XQQiIsqAfqjlw8rKSjg4OGhsK168uHjy5IkQQghLS0shhBAREREa+0RERMiPfSkwMFB8+PBB/nn69OmPFImIiIgymB8KH+XLlxe3b9/W2Hbnzh1RsGBBIURy51NLS0tx6NAh+fHIyEhx9uxZ4enpmepzGhgYCBMTE40fIiIi+nX90G2XAQMGiHLlyolJkyaJpk2binPnzomFCxeKhQsXCiGEkCRJ9O/fX0yYMEHY29uLQoUKiZEjR4q8efOKhg0bpkf5iYiIKIP5ofBRpkwZsXXrVhEYGCjGjRsnChUqJGbOnClatWol7zN06FARHR0tunbtKt6/fy8qVKgg9u7dKwwNDdO88ERERJTx/FD4EEKIunXrirp16371cUmSxLhx48S4ceP+VcGIiIjo18S1XYiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKepfhY8pU6YISZJE//795W0xMTGiV69ewtzcXBgbGws/Pz8RERHxb8tJREREv4ifDh/nz58XwcHBomTJkhrbBwwYIHbs2CE2btwojh07JsLCwoSvr++/LigRERH9Gn4qfERFRYlWrVqJRYsWiRw5csjbP3z4IJYsWSKmT58uqlSpIlxdXcWyZcvEn3/+Kc6cOZNmhSYiIqKM66fCR69evYSPj4+oVq2axvaLFy+K+Ph4je3FihUT1tbW4vTp06k+V2xsrIiMjNT4ISIiol+X3o/+wrp168SlS5fE+fPnUzwWHh4usmTJIszMzDS2W1hYiPDw8FSfb/LkyWLs2LE/WgzKIGwCdmm7CCk8muLzj/uw3Gnne8pNRP8tP9Ty8fTpU9GvXz+xevVqYWhomCYFCAwMFB8+fJB/nj59mibPS0RERLrph8LHxYsXxcuXL0Xp0qWFnp6e0NPTE8eOHROzZ88Wenp6wsLCQsTFxYn3799r/F5ERISwtLRM9TkNDAyEiYmJxg8RERH9un7otkvVqlXFtWvXNLZ16NBBFCtWTPj7+4sCBQoIfX19cejQIeHn5yeEEOL27dviyZMnwtPTM+1KTURERBnWD4WP7NmzC0dHR41t2bJlE+bm5vL2Tp06iYEDB4qcOXMKExMT0adPH+Hp6Sk8PDzSrtRERESUYf1wh9N/MmPGDJEpUybh5+cnYmNjRc2aNcX8+fPT+mWIiIgog/rX4ePo0aMa/zY0NBTz5s0T8+bN+7dPTURERL8gru1CREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFKWn7QIQEdkE7NJ2EVJ4NMXnH/fJqOUm0ja2fBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFE/FD4mT54sypQpI7Jnzy7y5MkjGjZsKG7fvq2xT0xMjOjVq5cwNzcXxsbGws/PT0RERKRpoYmIiCjj+qHwcezYMdGrVy9x5swZceDAAREfHy9q1KghoqOj5X0GDBggduzYITZu3CiOHTsmwsLChK+vb5oXnIiIiDImvR/Zee/evRr/Xr58uciTJ4+4ePGi8PLyEh8+fBBLliwRa9asEVWqVBFCCLFs2TJRvHhxcebMGeHh4ZF2JSciIqIM6V/1+fjw4YMQQoicOXMKIYS4ePGiiI+PF9WqVZP3KVasmLC2thanT59O9TliY2NFZGSkxg8RERH9un6o5UNdUlKS6N+/vyhfvrxwdHQUQggRHh4usmTJIszMzDT2tbCwEOHh4ak+z+TJk8XYsWN/thhERPSDbAJ2absIKTya4vOP+7Dcaed7yp2efrrlo1evXuL69eti3bp1/6oAgYGB4sOHD/LP06dP/9XzERERkW77qZaP3r17i507d4rjx4+L/Pnzy9stLS1FXFyceP/+vUbrR0REhLC0tEz1uQwMDISBgcHPFIOIiIgyoB9q+QAgevfuLbZu3SoOHz4sChUqpPG4q6ur0NfXF4cOHZK33b59Wzx58kR4enqmTYmJiIgoQ/uhlo9evXqJNWvWiG3btons2bPL/ThMTU2FkZGRMDU1FZ06dRIDBw4UOXPmFCYmJqJPnz7C09OTI12IiIhICPGD4WPBggVCCCEqV66ssX3ZsmWiffv2QgghZsyYITJlyiT8/PxEbGysqFmzppg/f36aFJaIiIgyvh8KHwD+cR9DQ0Mxb948MW/evJ8uFBEREf26uLYLERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpKt/Axb948YWNjIwwNDUXZsmXFuXPn0uuliIiIKANJl/Cxfv16MXDgQDF69Ghx6dIl4ezsLGrWrClevnyZHi9HREREGUi6hI/p06eLLl26iA4dOggHBwcRFBQksmbNKpYuXZoeL0dEREQZiF5aP2FcXJy4ePGiCAwMlLdlypRJVKtWTZw+fTrF/rGxsSI2Nlb+94cPH4QQQkRGRqZ10YQQQiTFfkqX5/03vudvZbnTDsutLJZbWSy3sn7lcv/scwL4552Rxp4/fw4hBP7880+N7UOG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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "top = df.head(10)\n",
        "plt.bar(top[\"name\"], top[\"score\"])\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 503
        },
        "id": "0qtQwGiVQLoy",
        "outputId": "c74493c4-2112-4043-c38f-c8d688970e63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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iIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRPxw+nj9/Llq3bi3Mzc2FkZGRcHJyEhcuXJAfByBGjRolrKyshJGRkahWrZq4e/dumhaaiIiIMq4fCh/v3r0T5cuXF/r6+mLPnj3i5s2b4o8//hA5cuSQ95k2bZqYPXu2CAoKEmfPnhXZsmUTNWvWFDExMWleeCIiIsp49H5k56lTp4oCBQqIZcuWydsKFSok/z8AMXPmTDFixAjRoEEDIYQQK1asEBYWFiI0NFQ0b948jYpNREREGdUPtXxs375duLm5iSZNmog8efKIUqVKiUWLFsmPP3z4UISHh4tq1arJ20xNTUXZsmXF6dOn067URERElGH9UPh48OCBWLBggbC3txf79u0TPXr0EH379hUhISFCCCHCw8OFEEJYWFho/J6FhYX82JdiY2NFZGSkxg8RERH9un7otktSUpJwc3MTkyZNEkIIUapUKXH9+nURFBQk2rVr91MFmDx5shg7duxP/e5/iU3ALm0XIYVHU3y0XQQiIsqAfqjlw8rKSjg4OGhsK168uHjy5IkQQghLS0shhBAREREa+0RERMiPfSkwMFB8+PBB/nn69OmPFImIiIgymB8KH+XLlxe3b9/W2Hbnzh1RsGBBIURy51NLS0tx6NAh+fHIyEhx9uxZ4enpmepzGhgYCBMTE40fIiIi+nX90G2XAQMGiHLlyolJkyaJpk2binPnzomFCxeKhQsXCiGEkCRJ9O/fX0yYMEHY29uLQoUKiZEjR4q8efOKhg0bpkf5iYiIKIP5ofBRpkwZsXXrVhEYGCjGjRsnChUqJGbOnClatWol7zN06FARHR0tunbtKt6/fy8qVKgg9u7dKwwNDdO88ERERJTx/FD4EEKIunXrirp16371cUmSxLhx48S4ceP+VcGIiIjo18S1XYiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKepfhY8pU6YISZJE//795W0xMTGiV69ewtzcXBgbGws/Pz8RERHxb8tJREREv4ifDh/nz58XwcHBomTJkhrbBwwYIHbs2CE2btwojh07JsLCwoSvr++/LigRERH9Gn4qfERFRYlWrVqJRYsWiRw5csjbP3z4IJYsWSKmT58uqlSpIlxdXcWyZcvEn3/+Kc6cOZNmhSYiIqKM66fCR69evYSPj4+oVq2axvaLFy+K+Ph4je3FihUT1tbW4vTp06k+V2xsrIiMjNT4ISIiol+X3o/+wrp168SlS5fE+fPnUzwWHh4usmTJIszMzDS2W1hYiPDw8FSfb/LkyWLs2LE/WgzKIGwCdmm7CCk8muLzj/uw3Gnne8pNRP8tP9Ty8fTpU9GvXz+xevVqYWhomCYFCAwMFB8+fJB/nj59mibPS0RERLrph8LHxYsXxcuXL0Xp0qWFnp6e0NPTE8eOHROzZ88Wenp6wsLCQsTFxYn3799r/F5ERISwtLRM9TkNDAyEiYmJxg8RERH9un7otkvVqlXFtWvXNLZ16NBBFCtWTPj7+4sCBQoIfX19cejQIeHn5yeEEOL27dviyZMnwtPTM+1KTURERBnWD4WP7NmzC0dHR41t2bJlE+bm5vL2Tp06iYEDB4qcOXMKExMT0adPH+Hp6Sk8PDzSrtRERESUYf1wh9N/MmPGDJEpUybh5+cnYmNjRc2aNcX8+fPT+mWIiIgog/rX4ePo0aMa/zY0NBTz5s0T8+bN+7dPTURERL8gru1CREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFKWn7QIQEdkE7NJ2EVJ4NMXnH/fJqOUm0ja2fBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFE/FD4mT54sypQpI7Jnzy7y5MkjGjZsKG7fvq2xT0xMjOjVq5cwNzcXxsbGws/PT0RERKRpoYmIiCjj+qHwcezYMdGrVy9x5swZceDAAREfHy9q1KghoqOj5X0GDBggduzYITZu3CiOHTsmwsLChK+vb5oXnIiIiDImvR/Zee/evRr/Xr58uciTJ4+4ePGi8PLyEh8+fBBLliwRa9asEVWqVBFCCLFs2TJRvHhxcebMGeHh4ZF2JSciIqIM6V/1+fjw4YMQQoicOXMKIYS4ePGiiI+PF9WqVZP3KVasmLC2thanT59O9TliY2NFZGSkxg8RERH9un6o5UNdUlKS6N+/vyhfvrxwdHQUQggRHh4usmTJIszMzDT2tbCwEOHh4ak+z+TJk8XYsWN/thhERPSDbAJ2absIKTya4vOP+7Dcaed7yp2efrrlo1evXuL69eti3bp1/6oAgYGB4sOHD/LP06dP/9XzERERkW77qZaP3r17i507d4rjx4+L/Pnzy9stLS1FXFyceP/+vUbrR0REhLC0tEz1uQwMDISBgcHPFIOIiIgyoB9q+QAgevfuLbZu3SoOHz4sChUqpPG4q6ur0NfXF4cOHZK33b59Wzx58kR4enqmTYmJiIgoQ/uhlo9evXqJNWvWiG3btons2bPL/ThMTU2FkZGRMDU1FZ06dRIDBw4UOXPmFCYmJqJPnz7C09OTI12IiIhICPGD4WPBggVCCCEqV66ssX3ZsmWiffv2QgghZsyYITJlyiT8/PxEbGysqFmzppg/f36aFJaIiIgyvh8KHwD+cR9DQ0Mxb948MW/evJ8uFBEREf26uLYLERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpi+CAiIiJFMXwQERGRohg+iIiISFEMH0RERKQohg8iIiJSFMMHERERKYrhg4iIiBTF8EFERESKYvggIiIiRTF8EBERkaIYPoiIiEhRDB9ERESkKIYPIiIiUhTDBxERESmK4YOIiIgUxfBBREREimL4ICIiIkUxfBAREZGiGD6IiIhIUQwfREREpCiGDyIiIlIUwwcREREpiuGDiIiIFMXwQURERIpKt/Axb948YWNjIwwNDUXZsmXFuXPn0uuliIiIKANJl/Cxfv16MXDgQDF69Ghx6dIl4ezsLGrWrClevnyZHi9HREREGUi6hI/p06eLLl26iA4dOggHBwcRFBQksmbNKpYuXZoeL0dEREQZiF5aP2FcXJy4ePGiCAwMlLdlypRJVKtWTZw+fTrF/rGxsSI2Nlb+94cPH4QQQkRGRqZ10YQQQiTFfkqX5/03vudvZbnTDsutLJZbWSy3sn7lcv/scwL4552Rxp4/fw4hBP7880+N7UOG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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.hist(df[\"score\"], bins=10)\n",
        "plt.title(\"Score Distribution\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "id": "4lPifBSuQ2Jg",
        "outputId": "4d70e935-1e5a-4e3e-b8bd-2217deb87868"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAGzCAYAAACPa3XZAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAKGlJREFUeJzt3Xt8TXe+//H3DrIjSBAkoonEZRq3Qd0GrcuR0oyh2qo6o07oDEPjNnqUnB6XVDWpmUdH61rOKaZ1n7ZqtKVOMKYV91LaadCGpow4ZkhcEyf7+/ujD/vX3UQqtfY3Eq/n47H+WN/13ev7+a6Q/c667O0yxhgBAABYElDWBQAAgLsL4QMAAFhF+AAAAFYRPgAAgFWEDwAAYBXhAwAAWEX4AAAAVhE+AACAVYQPAABgFeEDgKN69OihHj16WBnL5XJpxowZ3vUZM2bI5XLp3LlzVsaPiYnRsGHDrIwFVCSED8Bhhw8f1sCBA9WwYUMFBQWpQYMGevDBBzV37tyyLq3Uhg0bJpfL5V2qV6+uRo0aaeDAgXrrrbfk8XgcGWfnzp2aMWOGLly44Mj+nHQn1waUV5XLugCgItm5c6d69uyp6OhojRgxQhEREcrOztauXbv0yiuvaOzYsWVdYqm53W7913/9lyTp6tWrOnnypP785z9r4MCB6tGjh959912FhIR4+3/44YelHmPnzp1KSUnRsGHDVLNmzVt+3dWrV1W5sn9/jZVUW2ZmpgIC+BsOKC3CB+CgWbNmKTQ0VHv37i3yRnX27FmrtVy5ckXBwcG3vZ/KlSvrySef9Gl74YUXlJaWpuTkZI0YMUJr1qzxbgsMDLztMUvi8XhUUFCgoKAgBQUF+XWsH+J2u8t0fKC8IrIDDvryyy/VokWLYv96r1evXpG2N998Ux07dlRwcLBq1aqlbt26FTlzsGDBArVo0UJut1uRkZFKSkoqcgmgR48eatmypfbv369u3bopODhY//Ef/yFJys/P1/Tp09WkSRO53W5FRUXp2WefVX5+/m3NdcqUKerdu7fWrVuno0eP+tTy/Xs+5s6dqxYtWnjn2b59e61cuVLSt/dpTJo0SZIUGxvrvcRz4sQJSd/e1zFmzBitWLHCexw2bdrk3fbdez5uOHfunAYNGqSQkBCFhYVp/Pjxunbtmnf7iRMn5HK5tGzZsiKv/e4+f6i24u75+Oqrr/T444+rdu3aCg4O1s9+9jO99957Pn22b98ul8ultWvXatasWbrnnnsUFBSkXr166fjx4zc95kBFwZkPwEENGzZURkaGjhw5opYtW5bYNyUlRTNmzFCXLl30/PPPKzAwULt379bWrVvVu3dvSd+++aWkpCg+Pl6jR49WZmamFi5cqL179+rjjz9WlSpVvPv7xz/+oYSEBA0ePFhPPvmkwsPD5fF41L9/f3300UcaOXKkmjVrpsOHD+sPf/iDjh49qvXr19/WfIcOHaoPP/xQW7Zs0U9+8pNi+yxZskTjxo3TwIEDvSHg008/1e7du/XLX/5Sjz76qI4ePapVq1bpD3/4g+rUqSNJqlu3rncfW7du1dq1azVmzBjVqVNHMTExJdY1aNAgxcTEKDU1Vbt27dKrr76q8+fP649//GOp5ncrtX1XTk6OunTpoitXrmjcuHEKCwvT8uXL1b9/f/3pT3/SI4884tM/LS1NAQEB+vd//3fl5uZq9uzZGjJkiHbv3l2qOoFyxwBwzIcffmgqVapkKlWqZDp37myeffZZs3nzZlNQUODT79ixYyYgIMA88sgjprCw0Gebx+Mxxhhz9uxZExgYaHr37u3TZ968eUaSef31171t3bt3N5LMokWLfPb1xhtvmICAAPPXv/7Vp33RokVGkvn4449LnE9iYqKpVq3aTbd/8sknRpL57W9/61NL9+7dvesPP/ywadGiRYnj/O53vzOSTFZWVpFtkkxAQID57LPPit02ffp07/r06dONJNO/f3+ffk8//bSRZA4dOmSMMSYrK8tIMkuXLv3BfZZUW8OGDU1iYqJ3fcKECUaSz/G+ePGiiY2NNTExMd6f47Zt24wk06xZM5Ofn+/t+8orrxhJ5vDhw0XGAioSLrsADnrwwQeVkZGh/v3769ChQ5o9e7b69OmjBg0aaMOGDd5+69evl8fj0bRp04rcsOhyuSRJ//M//6OCggJNmDDBp8+IESMUEhJS5FS+2+3W8OHDfdrWrVunZs2aKS4uTufOnfMu//Iv/yJJ2rZt223Nt3r16pKkixcv3rRPzZo19c0332jv3r0/epzu3burefPmt9w/KSnJZ/3Gjb7vv//+j67hVrz//vvq2LGj7r//fm9b9erVNXLkSJ04cUKff/65T//hw4f73CPzwAMPSPr20g1QkRE+AId16NBBb7/9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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(df[\"ai_score\"], df[\"score\"])\n",
        "plt.xlabel(\"AI Score\")\n",
        "plt.ylabel(\"Final Score\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "8M70Sn8eQ3Vy",
        "outputId": "39336760-a7c9-4a8b-a533-cab7f417e756"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj4AAAGwCAYAAACpYG+ZAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAMztJREFUeJzt3XtUVXX+//HXAeSiwlG8cCDRSE3FW6lpZNm3xDSLshy/Zjl2W1ZGXtKp9NcoWSZmjTNppeWYVlpaLa1s1K+OOjjTgJqoiRhZUfJVDlTqAS8Iwf794dczHkHj6Llw2M/HWnst92d/2OfNZzFzXu392Z9tMQzDEAAAgAkE+bsAAAAAXyH4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0wjxdwF1SVVVlQ4dOqTIyEhZLBZ/lwMAAGrBMAyVlpYqLi5OQUEXvqZD8DnLoUOHFB8f7+8yAADARSgoKFCrVq0u2Ifgc5bIyEhJpwcuKirKz9UAAIDaKCkpUXx8vPN7/EIIPmc5c3srKiqK4AMAQICpzTQVJjcDAADTIPgAAADTIPgAAADTIPgAAADTIPgAAADTIPgAAADTIPgAAADTIPgAAADTIPgAAADTYOVmAADgdZVVhrblH1ZxaZlaRoard0K0goN8/0Jwgg8AAPCqdTmFmr46V4WOMmdbrDVcaSmJGtQl1qe1cKsLAAB4zbqcQo1Zmu0SeiTJ7ijTmKXZWpdT6NN6CD4AAMArKqsMTV+dK6OGY2fapq/OVWVVTT28g+ADAAC8Ylv+4WpXes5mSCp0lGlb/mGf1UTwAQAAXlFcev7QczH9PIHgAwAAvKJlZLhH+3kCwQcAAHhF74RoxVrDdb6H1i06/XRX74Ron9VE8AEAAF4RHGRRWkqiJFULP2f201ISfbqeD8EHAAB4zaAusZo/sodsVtfbWTZruOaP7OHzdXxYwBAAAHjVoC6xGpBoY+VmAABgDsFBFiW1bebvMrjVBQAAzIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATIPgAwAATCNggk9lZaWmTp2qhIQERUREqG3btnrhhRdkGIazj2EYmjZtmmJjYxUREaHk5GTt37/fj1UDAIC6JGCCz0svvaT58+frtdde0759+/TSSy9p9uzZmjdvnrPP7NmzNXfuXC1YsEBbt25Vo0aNNHDgQJWVlfmxcgAAUFdYjLMvmdRht99+u2JiYrRo0SJn29ChQxUREaGlS5fKMAzFxcVp0qRJ+sMf/iBJcjgciomJ0ZIlS3TPPff85meUlJTIarXK4XAoKirKa78LAADwHHe+vwPmis91112njRs36ptvvpEk7d69W//617906623SpLy8/Nlt9uVnJzs/Bmr1ao+ffooMzOzxnOeOnVKJSUlLhsAAKi/QvxdQG1NnjxZJSUl6tixo4KDg1VZWakXX3xR9913nyTJbrdLkmJiYlx+LiYmxnnsXOnp6Zo+fbp3CwcAAHVGwFzx+fDDD7Vs2TK9//77ys7O1jvvvKNXXnlF77zzzkWfc8qUKXI4HM6toKDAgxUDAIC6JmCu+Dz11FOaPHmyc65O165d9eOPPyo9PV3333+/bDabJKmoqEixsbHOnysqKtJVV11V4znDwsIUFhbm9doBAEDdEDBXfE6cOKGgINdyg4ODVVVVJUlKSEiQzWbTxo0bncdLSkq0detWJSUl+bRWAABQNwXMFZ+UlBS9+OKLat26tTp37qydO3dqzpw5euihhyRJFotFEyZM0IwZM9S+fXslJCRo6tSpiouL05AhQ/xbPAAAqBMCJvjMmzdPU6dO1eOPP67i4mLFxcXp0Ucf1bRp05x9nn76aR0/flyPPPKIjh49quuvv17r1q1TeHi4HysHAAB1RcCs4+MLrOMDAEDgqZfr+AAAAFwqgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADANgg8AADCNEH8XAACAP1VWGdqWf1jFpWVqGRmu3gnRCg6y+LsseElAXfE5ePCgRo4cqWbNmikiIkJdu3bVl19+6TxuGIamTZum2NhYRUREKDk5Wfv37/djxQCAumxdTqGuf2mTRizM0vjluzRiYZau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Fouxfv16wzAYY286+6kuw2CsPWHSpEnGP/7xDyM/P9/44osvjOTkZKN58+ZGcXGxYRj+H2OCjw/MmzfPaN26tREaGmr07t3byMrK8ndJAW/z5s2GpGrb/fffbxjG6Ufap06dasTExBhhYWFG//79jby8PP8WHYBqGmNJxuLFi519Tp48aTz++ONG06ZNjYYNGxp33XWXUVhY6L+iA9BDDz1ktGnTxggNDTVatGhh9O/f3xl6DIMx9qZzgw9jfemGDx9uxMbGGqGhocZll11mDB8+3Pj222+dx/09xhbDMAzfXFsCAADwL+b4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AAAA0yD4AKgTMjMzFRwcrNtuu63asR9++EEWi0W7du0678/n5+fr3nvvVVxcnMLDw9WqVSvdeeed+vrrr71YNYBAQ/ABUCcsWrRIY8eO1ZYtW3To0CG3fraiokIDBgyQw+HQypUrlZeXpxUrVqhr1646evSodwr+v88FEFgIPgD87tixY1qxYoXGjBmj2267TUuWLHHr5/fu3avvvvtOb7zxhq699lq1adNGffv21YwZM3Tttdc6+/3v//6vRowYoejoaDVq1Ei9evXS1q1bncfnz5+vtm3bKjQ0VB06dNB7773n8jkWi0Xz58/XHXfcoUaNGunFF1+UJH366afq0aOHwsPDdcUVV2j69On69ddfL35AAHgNwQeA33344Yfq2LGjOnTooJEjR+rtt9+WO+9PbtGihYKCgvTxxx+rsrKyxj7Hjh3TjTfeqIMHD+qzzz7T7t279fTTT6uqqkqStGrVKo0fP16TJk1STk6OHn30UT344IPavHmzy3mee+453XXXXdqzZ48eeugh/fOf/9SoUaM0fvx45ebm6s0339SSJUucoQhAHeOz98ADwHlcd911xl/+8hfDMAyjoqLCaN68ubF582bn8fz8fEOSsXPnzvOe47XXXjMaNmxoREZGGjfddJPx/PPPG999953z+JtvvmlERkYav/zyy3lrGD16tEvbsGHDjMGDBzv3JRkTJkxw6dO/f39j5syZLm3vvfeeERsbe8HfGYB/cMUHgF/l5eVp27ZtGjFihCQpJCREw4cP16JFi9w6T2pqqux2u5YtW6akpCR99NFH6ty5szZs2CBJ2rVrl66++mpFR0fX+PP79u1T3759Xdr69u2rffv2ubT16tXLZX/37t16/vnn1bhxY+c2evRoFRYW6sSJE279DgC8L8TfBQAwt0WLFunXX39VXFycs80wDIWFhem1116T1Wqt9bkiIyOVkpKilJQUzZgxQwMHDtSMGTM0YMAARUREeKTeRo0auewfO3ZM06dP1913312tb3h4uEc+E4DncMUHgN/8+uuvevfdd/WnP/1Ju3btcm67d+9WXFycPvjgg4s+t8ViUceOHXX8+HFJUrdu3bRr1y4dPny4xv6dOnXSF1984dL2xRdfKDEx8YKf06NHD+Xl5aldu3bVtqAg/i8WqGu44gPAbz7//HMdOXJEDz/8cLUrO0OHDtWiRYv02GOP/eZ5du3apbS0NP3+979XYmKiQkNDlZGRobffflvPPPOMJGnEiBGaOXOmhgwZovT0dMXGxmrnzp2Ki4tTUlKSnnrqKf33f/+3rr76aiUnJ2v16tVauXKl/v73v1/ws6dNm6bbb79drVu31u9+9zsFBQVp9+7dysnJ0YwZMy5+cAB4h78nGQEwr9tvv91l8vDZtm7dakgydu/e/ZuTm3/66Sdj3LhxRpcuXYzGjRsbkZGRRteuXY1XXnnFqKysdPb74YcfjKFDhxpRUVFGw4YNjV69ehlbt251Hn/jjTeMK664wmjQoIFx5ZVXGu+++67L50gyVq1aVe3z161bZ1x33XVGRESEERUVZfTu3dt466233B8QAF5nMQw3nhkFAAAIYNyABgAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApkHwAQAApvH/ARdrUEXU9fpMAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "import ast\n",
        "\n",
        "# Convert string representations of lists to actual lists\n",
        "df[\"matched\"] = df[\"matched\"].apply(ast.literal_eval)\n",
        "\n",
        "all_skills = sum(df[\"matched\"], [])\n",
        "skill_count = Counter(all_skills)\n",
        "\n",
        "top_skills = skill_count.most_common(10)\n",
        "\n",
        "skills, counts = zip(*top_skills)\n",
        "\n",
        "plt.bar(skills, counts)\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 553
        },
        "id": "dWYLTAxeQ6Dm",
        "outputId": "cf2c95eb-c2a4-44df-f28f-8776e343d4ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiMAAAIYCAYAAAC/l+zfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAbJdJREFUeJzt3XdUFNffBvBnKSJGwEpREbBhpYgNu8beY+xGrBh7i6CoiVGj2Dv2giWKvfeuUayosUT92RugYkEQaft9/+BlwooaUXQWeD7n7DkyO7N7x5mdeebOvXc0IiIgIiIiUomB2gUgIiKijI1hhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKiO1C/AptFotHj9+DDMzM2g0GrWLQ0RERJ9ARPD69WvkyZMHBgYfrv9IE2Hk8ePHsLW1VbsYRERE9BkePHiAfPnyffD9NBFGzMzMACSsjLm5ucqlISIiok8RHh4OW1tb5Tz+IWkijCTemjE3N2cYISIiSmP+q4kFG7ASERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkqhSFkblz58LJyUl5Roy7uzt27dr10WXWrVuHokWLInPmzChVqhR27tz5RQUmIiKi9CVFYSRfvnwYP348zp07h7Nnz6JmzZpo2rQprly58t75T5w4gbZt26Jr1644f/48mjVrhmbNmuHy5cupUngiIiJK+zQiIl/yATly5MCkSZPQtWvXZO+1bt0akZGR2L59uzKtQoUKcHFxwbx58z75O8LDw2FhYYFXr17xqb1ERERpxKeevz+7zUh8fDwCAgIQGRkJd3f3984TGBiIWrVq6UyrW7cuAgMDP/rZ0dHRCA8P13kRERFR+mSU0gUuXboEd3d3vH37FlmzZsWmTZtQvHjx984bEhICKysrnWlWVlYICQn56Hf4+vpi1KhRKS3aZ7EfuuObfE9K3B3f8D/nYblTD8v9baXnchPR50lxzYijoyMuXLiAU6dOoWfPnujYsSOuXr2aqoXy8fHBq1evlNeDBw9S9fOJiIhIf6S4ZiRTpkwoVKgQAMDNzQ1nzpzBjBkzMH/+/GTzWltbIzQ0VGdaaGgorK2tP/odJiYmMDExSWnRiIiIKA364nFGtFotoqOj3/ueu7s7Dhw4oDNt3759H2xjQkRERBlPimpGfHx8UL9+feTPnx+vX7/GqlWrcPjwYezZswcA4OHhgbx588LX1xcA0L9/f1SrVg1TpkxBw4YNERAQgLNnz2LBggWpvyZERESUJqUojDx58gQeHh4IDg6GhYUFnJycsGfPHtSuXRsAcP/+fRgY/FvZUrFiRaxatQojRozAsGHDULhwYWzevBklS5ZM3bUgIiKiNCtFYWTx4sUfff/w4cPJprVs2RItW7ZMUaGIiIgo4+CzaYiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkapSFEZ8fX1RtmxZmJmZwdLSEs2aNcP169c/uoy/vz80Go3OK3PmzF9UaCIiIko/UhRGjhw5gt69e+PkyZPYt28fYmNjUadOHURGRn50OXNzcwQHByuve/fufVGhiYiIKP0wSsnMu3fv1vnb398flpaWOHfuHKpWrfrB5TQaDaytrT+vhERERJSufVGbkVevXgEAcuTI8dH5IiIiYGdnB1tbWzRt2hRXrlz56PzR0dEIDw/XeREREVH69NlhRKvVYsCAAahUqRJKliz5wfkcHR2xZMkSbNmyBStXroRWq0XFihXx8OHDDy7j6+sLCwsL5WVra/u5xSQiIiI999lhpHfv3rh8+TICAgI+Op+7uzs8PDzg4uKCatWqYePGjcidOzfmz5//wWV8fHzw6tUr5fXgwYPPLSYRERHpuRS1GUnUp08fbN++HUePHkW+fPlStKyxsTFcXV1x8+bND85jYmICExOTzykaERERpTEpqhkREfTp0webNm3CwYMH4eDgkOIvjI+Px6VLl2BjY5PiZYmIiCj9SVHNSO/evbFq1Sps2bIFZmZmCAkJAQBYWFjA1NQUAODh4YG8efPC19cXADB69GhUqFABhQoVwsuXLzFp0iTcu3cP3bp1S+VVISIiorQoRWFk7ty5AIDq1avrTF+6dCk6deoEALh//z4MDP6tcHnx4gU8PT0REhKC7Nmzw83NDSdOnEDx4sW/rORERESULqQojIjIf85z+PBhnb+nTZuGadOmpahQRERElHHw2TRERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkapSFEZ8fX1RtmxZmJmZwdLSEs2aNcP169f/c7l169ahaNGiyJw5M0qVKoWdO3d+doGJiIgofUlRGDly5Ah69+6NkydPYt++fYiNjUWdOnUQGRn5wWVOnDiBtm3bomvXrjh//jyaNWuGZs2a4fLly19ceCIiIkr7jFIy8+7du3X+9vf3h6WlJc6dO4eqVau+d5kZM2agXr168PLyAgCMGTMG+/btw+zZszFv3rzPLDYRERGlF1/UZuTVq1cAgBw5cnxwnsDAQNSqVUtnWt26dREYGPjBZaKjoxEeHq7zIiIiovQpRTUjSWm1WgwYMACVKlVCyZIlPzhfSEgIrKysdKZZWVkhJCTkg8v4+vpi1KhRn1s0IiJV2A/doXYRkrk7vuF/zpNWy03px2fXjPTu3RuXL19GQEBAapYHAODj44NXr14prwcPHqT6dxAREZF++KyakT59+mD79u04evQo8uXL99F5ra2tERoaqjMtNDQU1tbWH1zGxMQEJiYmn1M0IiIiSmNSVDMiIujTpw82bdqEgwcPwsHB4T+XcXd3x4EDB3Sm7du3D+7u7ikrKREREaVLKaoZ6d27N1atWoUtW7bAzMxMafdhYWEBU1NTAICHhwfy5s0LX19fAED//v1RrVo1TJkyBQ0bNkRAQADOnj2LBQsWpPKqEBERUVqUopqRuXPn4tWrV6hevTpsbGyU15o1a5R57t+/j+DgYOXvihUrYtWqVViwYAGcnZ2xfv16bN68+aONXomIiCjjSFHNiIj85zyHDx9ONq1ly5Zo2bJlSr6KiIiIMgg+m4aIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREakqxWHk6NGjaNy4MfLkyQONRoPNmzd/dP7Dhw9Do9Eke4WEhHxumYmIiCgdSXEYiYyMhLOzM/z8/FK03PXr1xEcHKy8LC0tU/rVRERElA4ZpXSB+vXro379+in+IktLS2TLli3FyxEREVH69s3ajLi4uMDGxga1a9fG8ePHPzpvdHQ0wsPDdV5ERESUPn31MGJjY4N58+Zhw4YN2LBhA2xtbVG9enUEBQV9cBlfX19YWFgoL1tb269dTCIiIlJJim/TpJSjoyMcHR2VvytWrIhbt25h2rRpWLFixXuX8fHxwaBBg5S/w8PDGUiIiIjSqa8eRt6nXLly+Ouvvz74vomJCUxMTL5hiYiIiEgtqowzcuHCBdjY2Kjx1URERKRnUlwzEhERgZs3byp/37lzBxcuXECOHDmQP39++Pj44NGjR1i+fDkAYPr06XBwcECJEiXw9u1bLFq0CAcPHsTevXtTby2IiIgozUpxGDl79ixq1Kih/J3YtqNjx47w9/dHcHAw7t+/r7wfExODX375BY8ePUKWLFng5OSE/fv363wGERERZVwpDiPVq1eHiHzwfX9/f52/vb294e3tneKCERERUcbAZ9MQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVpTiMHD16FI0bN0aePHmg0WiwefPm/1zm8OHDKF26NExMTFCoUCH4+/t/RlGJiIgoPUpxGImMjISzszP8/Pw+af47d+6gYcOGqFGjBi5cuIABAwagW7du2LNnT4oLS0REROmPUUoXqF+/PurXr//J88+bNw8ODg6YMmUKAKBYsWL466+/MG3aNNStWzelX09ERETpzFdvMxIYGIhatWrpTKtbty4CAwM/uEx0dDTCw8N1XkRERJQ+pbhmJKVCQkJgZWWlM83Kygrh4eGIioqCqalpsmV8fX0xatSor100IiJKw+yH7lC7CMncHd/wP+dJq+X+mvSyN42Pjw9evXqlvB48eKB2kYiIiOgr+eo1I9bW1ggNDdWZFhoaCnNz8/fWigCAiYkJTExMvnbRiIiISA989ZoRd3d3HDhwQGfavn374O7u/rW/moiIiNKAFIeRiIgIXLhwARcuXACQ0HX3woULuH//PoCEWyweHh7K/D169MDt27fh7e2Na9euYc6cOVi7di0GDhyYOmtAREREaVqKw8jZs2fh6uoKV1dXAMCgQYPg6uqK3377DQAQHBysBBMAcHBwwI4dO7Bv3z44Oztj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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.sort_values(\"score\", ascending=False)\n",
        "df.reset_index(drop=True, inplace=True)"
      ],
      "metadata": {
        "id": "peKRaBJzRcJD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"rank\"] = df[\"score\"].rank(method=\"dense\", ascending=False)"
      ],
      "metadata": {
        "id": "ujrSOZmdShqE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"reason\"] = df.apply(\n",
        "    lambda x: f\"{len(x['matched'])} skills matched | AI score: {x['ai_score']}\",\n",
        "    axis=1\n",
        ")"
      ],
      "metadata": {
        "id": "UB0e0lIJSl85"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "final_output = df[[\"rank\", \"id\", \"name\", \"title\", \"score\", \"reason\"]]\n",
        "\n",
        "final_output.to_csv(\"FINAL_CANDIDATE_RANKING.csv\", index=False)\n",
        "\n",
        "print(\"FINAL PROJECT FILE READY 🚀\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bl2ejK0aSoTx",
        "outputId": "add24c91-2eb4-4e0a-b552-07cd6be12538"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "FINAL PROJECT FILE READY 🚀\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "top = df.head(10)\n",
        "\n",
        "plt.bar(top[\"name\"], top[\"score\"])\n",
        "plt.xticks(rotation=45)\n",
        "plt.title(\"Top 10 Candidates\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 525
        },
        "id": "9k5z02DSSwL-",
        "outputId": "6f95e4f4-45e2-493c-ba1c-144201ccd1bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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GD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJoyM3YBtOY0ZJexi5DI3cn+xi4CERGRZljzQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaa+KnzExcXJiBEjJF++fGJlZSXOzs4ybtw4AaCuA0BGjhwpDg4OYmVlJVWrVpWbN28me8GJiIgodfqq8DFlyhSZP3++zJkzR/744w+ZMmWKTJ06VWbPnq2uM3XqVJk1a5YsWLBATp06JRkyZJAaNWpIVFRUsheeiIiIUh+zr1n5f//7n9SvX1/8/f1FRMTJyUnWrVsnp0+fFpGEWo8ZM2bI8OHDpX79+iIisnLlSrGzs5PQ0FBp3rx5otf8+PGjfPz4Uf07IiLiH38YIiIiMn1fVfNRpkwZOXjwoNy4cUNERC5cuCDHjh2TWrVqiYjInTt3JCwsTKpWrao+J1OmTFK6dGk5ceJEkq85adIkyZQpk/ovT548//SzEBERUSrwVTUfQ4YMkYiICClSpIikTZtW4uLiZMKECdKqVSsREQkLCxMRETs7O4Pn2dnZqY99KigoSPr166f+HRERwQBCRET0Dfuq8LFx40ZZs2aNrF27VooVKya///679OnTR3LmzCmBgYH/qAAWFhZiYWHxj55LREREqc9XhY+BAwfKkCFD1LYbbm5ucu/ePZk0aZIEBgaKvb29iIiEh4eLg4OD+rzw8HDx8PBIvlITERFRqvVVbT7ev38vadIYPiVt2rQSHx8vIiL58uUTe3t7OXjwoPp4RESEnDp1Snx9fZOhuERERJTafVXNR926dWXChAni6OgoxYoVk99++02mTZsmHTp0EBERRVGkT58+Mn78eClYsKDky5dPRowYITlz5pQGDRqkRPmJiIgolfmq8DF79mwZMWKEdOvWTZ4+fSo5c+aUzp07y8iRI9V1Bg0aJJGRkdKpUyd5/fq1lCtXTn7++WextLRM9sITERFR6qNAf3hSExARESGZMmWSN2/eiI2NTbK/vtOQXcn+mv/W3cn+xi4CERHRv/I152/O7UJERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRpr46fDx69Ehat24t2bJlEysrK3Fzc5OzZ8+qjwOQkSNHioODg1hZWUnVqlXl5s2byVpoIiIiSr2+Kny8evVKypYtK+bm5rJnzx65evWq/PTTT5IlSxZ1nalTp8qsWbNkwYIFcurUKcmQIYPUqFFDoqKikr3wRERElPqYfc3KU6ZMkTx58siyZcvUZfny5VP/H4DMmDFDhg8fLvXr1xcRkZUrV4qdnZ2EhoZK8+bNk6nYRERElFp9Vc3H9u3bxcvLS5o0aSI5cuSQEiVKyKJFi9TH79y5I2FhYVK1alV1WaZMmaR06dJy4sSJJF/z48ePEhERYfCPiIiIvl1fVfNx+/ZtmT9/vvTr10+GDh0qZ86ckV69ekm6dOkkMDBQwsLCRETEzs7O4Hl2dnbqY5+aNGmSjBkz5h8W/7/DacguYxchkbuT/Y1dBCIiSoW+quYjPj5eSpYsKRMnTpQSJUpIp06d5Pvvv5cFCxb84wIEBQXJmzdv1H8PHjz4x69FREREpu+rwoeDg4O4uLgYLCtatKjcv39fRETs7e1FRCQ8PNxgnfDwcPWxT1lYWIiNjY3BPyIiIvp2fVX4KFu2rFy/ft1g2Y0bNyRv3rwiktD41N7eXg4ePKg+HhERIadOnRJfX99kKC4RERGldl/V5qNv375SpkwZmThxojRt2lROnz4twcHBEhwcLCIiiqJInz59ZPz48VKwYEHJly+fjBgxQnLmzCkNGjRIifITERFRKvNV4aNUqVKydetWCQoKkrFjx0q+fPlkxowZ0qpVK3WdQYMGSWRkpHTq1Elev34t5cqVk59//lksLS2TvfBERESU+nxV+BARqVOnjtSpU+ezjyuKImPHjpWxY8f+q4IRERHRt4lzuxAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkqX8VPiZPniyKokifPn3UZVFRUdK9e3fJli2bWFtbS6NGjSQ8PPzflpOIiIi+Ef84fJw5c0YWLlwoxYsXN1jet29f2bFjh2zatEl+/fVXefz4sQQEBPzrghIREdG34R+Fj3fv3kmrVq1k0aJFkiVLFnX5mzdvZMmSJTJt2jSpXLmyeHp6yrJly+R///ufnDx5MtkKTURERKnXPwof3bt3F39/f6latarB8nPnzklMTIzB8iJFioijo6OcOHEiydf6+PGjREREGPwjIiKib5fZ1z5h/fr1cv78eTlz5kyix8LCwiRdunSSOXNmg+V2dnYSFhaW5OtNmjRJxowZ87XFoFTCacguYxchkbuT/f92HZY7+XxJuYnov+Wraj4ePHggvXv3ljVr1oilpWWyFCAoKEjevHmj/nvw4EGyvC4RERGZpq8KH+fOnZOnT59KyZIlxczMTMzMzOTXX3+VWbNmiZmZmdjZ2Ul0dLS8fv3a4Hnh4eFib2+f5GtaWFiIjY2NwT8iIiL6dn3VbZcqVarIpUuXDJa1b99eihQpIoMHD5Y8efKIubm5HDx4UBo1aiQiItevX5f79++Lr69v8pWaiIiIUq2vCh8ZM2YUV1dXg2UZMmSQbNmyqcs7duwo/fr1k6xZs4qNjY307NlTfH19xcfHJ/lKTURERKnWVzc4/TvTp0+XNGnSSKNGjeTjx49So0YNmTdvXnK/DREREaVS/zp8HD582OBvS0tLmTt3rsydO/ffvjQRERF9gzi3CxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItKUmbELQETkNGSXsYuQyN3J/n+7TmotN5GxseaDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RERKQphg8iIiLSFMMHERERaYrhg4iIiDTF8EFERESaYvggIiIiTTF8EBERkaYYPoiIiEhTDB9ERESkKYYPIiIi0hTDBxEREWmK4YOIiIg0xfBBREREmmL4ICIiIk0xfBAREZGmGD6IiIhIUwwfREREpCmGDyIiItIUwwcRERFpiuGDiIiINMXwQURERJpi+CAiIiJNMXwQERGRphg+iIiISFMMH0RE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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.hist(df[\"score\"], bins=10)\n",
        "plt.title(\"Score Distribution\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "id": "sgEy5JCaSxYp",
        "outputId": "23b77d6d-ed31-417c-e9b5-a46f8beabd77"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAGzCAYAAACPa3XZAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAKGlJREFUeJzt3Xt8TXe+//H3DrIjSBAkoonEZRq3Qd0GrcuR0oyh2qo6o07oDEPjNnqUnB6XVDWpmUdH61rOKaZ1n7ZqtKVOMKYV91LaadCGpow4ZkhcEyf7+/ujD/vX3UQqtfY3Eq/n47H+WN/13ev7+a6Q/c667O0yxhgBAABYElDWBQAAgLsL4QMAAFhF+AAAAFYRPgAAgFWEDwAAYBXhAwAAWEX4AAAAVhE+AACAVYQPAABgFeEDgKN69OihHj16WBnL5XJpxowZ3vUZM2bI5XLp3LlzVsaPiYnRsGHDrIwFVCSED8Bhhw8f1sCBA9WwYUMFBQWpQYMGevDBBzV37tyyLq3Uhg0bJpfL5V2qV6+uRo0aaeDAgXrrrbfk8XgcGWfnzp2aMWOGLly44Mj+nHQn1waUV5XLugCgItm5c6d69uyp6OhojRgxQhEREcrOztauXbv0yiuvaOzYsWVdYqm53W7913/9lyTp6tWrOnnypP785z9r4MCB6tGjh959912FhIR4+3/44YelHmPnzp1KSUnRsGHDVLNmzVt+3dWrV1W5sn9/jZVUW2ZmpgIC+BsOKC3CB+CgWbNmKTQ0VHv37i3yRnX27FmrtVy5ckXBwcG3vZ/KlSvrySef9Gl74YUXlJaWpuTkZI0YMUJr1qzxbgsMDLztMUvi8XhUUFCgoKAgBQUF+XWsH+J2u8t0fKC8IrIDDvryyy/VokWLYv96r1evXpG2N998Ux07dlRwcLBq1aqlbt26FTlzsGDBArVo0UJut1uRkZFKSkoqcgmgR48eatmypfbv369u3bopODhY//Ef/yFJys/P1/Tp09WkSRO53W5FRUXp2WefVX5+/m3NdcqUKerdu7fWrVuno0eP+tTy/Xs+5s6dqxYtWnjn2b59e61cuVLSt/dpTJo0SZIUGxvrvcRz4sQJSd/e1zFmzBitWLHCexw2bdrk3fbdez5uOHfunAYNGqSQkBCFhYVp/Pjxunbtmnf7iRMn5HK5tGzZsiKv/e4+f6i24u75+Oqrr/T444+rdu3aCg4O1s9+9jO99957Pn22b98ul8ultWvXatasWbrnnnsUFBSkXr166fjx4zc95kBFwZkPwEENGzZURkaGjhw5opYtW5bYNyUlRTNmzFCXLl30/PPPKzAwULt379bWrVvVu3dvSd+++aWkpCg+Pl6jR49WZmamFi5cqL179+rjjz9WlSpVvPv7xz/+oYSEBA0ePFhPPvmkwsPD5fF41L9/f3300UcaOXKkmjVrpsOHD+sPf/iDjh49qvXr19/WfIcOHaoPP/xQW7Zs0U9+8pNi+yxZskTjxo3TwIEDvSHg008/1e7du/XLX/5Sjz76qI4ePapVq1bpD3/4g+rUqSNJqlu3rncfW7du1dq1azVmzBjVqVNHMTExJdY1aNAgxcTEKDU1Vbt27dKrr76q8+fP649//GOp5ncrtX1XTk6OunTpoitXrmjcuHEKCwvT8uXL1b9/f/3pT3/SI4884tM/LS1NAQEB+vd//3fl5uZq9uzZGjJkiHbv3l2qOoFyxwBwzIcffmgqVapkKlWqZDp37myeffZZs3nzZlNQUODT79ixYyYgIMA88sgjprCw0Gebx+Mxxhhz9uxZExgYaHr37u3TZ968eUaSef31171t3bt3N5LMokWLfPb1xhtvmICAAPPXv/7Vp33RokVGkvn4449LnE9iYqKpVq3aTbd/8sknRpL57W9/61NL9+7dvesPP/ywadGiRYnj/O53vzOSTFZWVpFtkkxAQID57LPPit02ffp07/r06dONJNO/f3+ffk8//bSRZA4dOmSMMSYrK8tIMkuXLv3BfZZUW8OGDU1iYqJ3fcKECUaSz/G+ePGiiY2NNTExMd6f47Zt24wk06xZM5Ofn+/t+8orrxhJ5vDhw0XGAioSLrsADnrwwQeVkZGh/v3769ChQ5o9e7b69OmjBg0aaMOGDd5+69evl8fj0bRp04rcsOhyuSRJ//M//6OCggJNmDDBp8+IESMUEhJS5FS+2+3W8OHDfdrWrVunZs2aKS4uTufOnfMu//Iv/yJJ2rZt223Nt3r16pKkixcv3rRPzZo19c0332jv3r0/epzu3burefPmt9w/KSnJZ/3Gjb7vv//+j67hVrz//vvq2LGj7r//fm9b9erVNXLkSJ04cUKff/65T//hw4f73CPzwAMPSPr20g1QkRE+AId16NBBb7/9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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "\n",
        "skills = sum(df[\"matched\"], [])\n",
        "skill_counts = Counter(skills)\n",
        "\n",
        "top_skills = skill_counts.most_common(10)\n",
        "\n",
        "names, counts = zip(*top_skills)\n",
        "\n",
        "plt.bar(names, counts)\n",
        "plt.xticks(rotation=45)\n",
        "plt.title(\"Top Required Skills\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "EA-2jyZnS_67",
        "outputId": "976e656a-0e7f-42f1-b0b1-f89debfdab05",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 575
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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kaCgINSsWVNnWp06dRAUFPTeZWJjYxEREaHzICIioowp1TUjqRUaGgpLS0udaZaWloiIiEBMTAxMTU1TLOPj44MxY8Z86aIREVE6Zjdsl9pFSOHupAb/OU96LfeXpJe9aby9vfHy5Uvl8eDBA7WLRERERF/IF68ZsbKyQlhYmM60sLAwmJubv7NWBABMTExgYmLypYtGREREeuCL14y4ubnhwIEDOtMCAwPh5ub2pVdNRERE6UCqw0hUVBQuXLiACxcuAHjTdffChQu4f/8+gDeXWDp06KDM36tXL9y+fRteXl64du0a/Pz8sH79egwaNChttoCIiIjStVSHkbNnz8LFxQUuLi4AgMGDB8PFxQW//fYbACAkJEQJJgBgb2+PXbt2ITAwEE5OTpg+fTqWLFnCbr1EREQE4BPajFSrVg0i8t7X3zW6arVq1XD+/PnUroqIiIi+AXrZm4aIiIi+HQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqGEaIiIhIVQwjREREpCqGESIiIlIVwwgRERGpimGEiIiIVMUwQkRERKpiGCEiIiJVMYwQERGRqhhGiIiISFUMI0RERKQqhhEiIiJSFcMIERERqYphhIiIiFTFMEJERESqYhghIiIiVTGMEBERkaoYRoiIiEhVDCNERESkKoYRIiIiUhXDCBEREamKYYSIiIhUxTBCREREqmIYISIiIlUxjBAREZGqPimM+Pr6ws7ODpkzZ0b58uVx+vTp987r7+8PjUaj88icOfMnF5iIiIgyllSHkXXr1mHw4MEYNWoUgoOD4eTkhDp16uDx48fvXcbc3BwhISHK4969e59VaCIiIso4Uh1GZsyYge7du6Nz584oVqwYFixYgCxZsmDZsmXvXUaj0cDKykp5WFpafnAdsbGxiIiI0HkQERFRxpSqMBIXF4dz586hZs2a/3sDAwPUrFkTQUFB710uKioKtra2sLGxQZMmTXDlypUPrsfHxwfZs2dXHjY2NqkpJhEREaUjqQojT58+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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv(\"FINAL_CANDIDATE_RANKING.csv\")\n",
        "df.head()"
      ],
      "metadata": {
        "id": "OmsrNEYVTDuz",
        "outputId": "98cb3ff6-157c-4cd0-a513-bd91ecec6641",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   rank            id            name                            title  score  \\\n",
              "0   1.0  CAND_0000031       Ela Singh  Recommendation Systems Engineer     90   \n",
              "1   2.0  CAND_0000001        Ira Vora                 Backend Engineer     60   \n",
              "2   3.0  CAND_0000032  Pranav Agarwal                   .NET Developer     40   \n",
              "3   3.0  CAND_0000038    Myra Trivedi                   Java Developer     40   \n",
              "4   3.0  CAND_0000043       Aarav Sen                   Cloud Engineer     40   \n",
              "\n",
              "                            reason  \n",
              "0  5 skills matched | AI score: 50  \n",
              "1  4 skills matched | AI score: 40  \n",
              "2  2 skills matched | AI score: 20  \n",
              "3  2 skills matched | AI score: 20  \n",
              "4  2 skills matched | AI score: 20  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3f39abbb-1b63-42b7-b958-e63f76841a47\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>rank</th>\n",
              "      <th>id</th>\n",
              "      <th>name</th>\n",
              "      <th>title</th>\n",
              "      <th>score</th>\n",
              "      <th>reason</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0</td>\n",
              "      <td>CAND_0000031</td>\n",
              "      <td>Ela Singh</td>\n",
              "      <td>Recommendation Systems Engineer</td>\n",
              "      <td>90</td>\n",
              "      <td>5 skills matched | AI score: 50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2.0</td>\n",
              "      <td>CAND_0000001</td>\n",
              "      <td>Ira Vora</td>\n",
              "      <td>Backend Engineer</td>\n",
              "      <td>60</td>\n",
              "      <td>4 skills matched | AI score: 40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3.0</td>\n",
              "      <td>CAND_0000032</td>\n",
              "      <td>Pranav Agarwal</td>\n",
              "      <td>.NET Developer</td>\n",
              "      <td>40</td>\n",
              "      <td>2 skills matched | AI score: 20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3.0</td>\n",
              "      <td>CAND_0000038</td>\n",
              "      <td>Myra Trivedi</td>\n",
              "      <td>Java Developer</td>\n",
              "      <td>40</td>\n",
              "      <td>2 skills matched | AI score: 20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>3.0</td>\n",
              "      <td>CAND_0000043</td>\n",
              "      <td>Aarav Sen</td>\n",
              "      <td>Cloud Engineer</td>\n",
              "      <td>40</td>\n",
              "      <td>2 skills matched | AI score: 20</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3f39abbb-1b63-42b7-b958-e63f76841a47')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-3f39abbb-1b63-42b7-b958-e63f76841a47 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-3f39abbb-1b63-42b7-b958-e63f76841a47');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 50,\n  \"fields\": [\n    {\n      \"column\": \"rank\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.6249198238484643,\n        \"min\": 1.0,\n        \"max\": 11.0,\n        \"num_unique_values\": 11,\n        \"samples\": [\n          6.0,\n          1.0,\n          10.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"id\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 50,\n        \"samples\": [\n          \"CAND_0000011\",\n          \"CAND_0000042\",\n          \"CAND_0000014\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 49,\n        \"samples\": [\n          \"Deepak Desai\",\n          \"Sai Saxena\",\n          \"Vikram Mittal\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"title\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 22,\n        \"samples\": [\n          \"Recommendation Systems Engineer\",\n          \"Mobile Developer\",\n          \"Civil Engineer\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": -50,\n        \"max\": 90,\n        \"num_unique_values\": 11,\n        \"samples\": [\n          10,\n          90,\n          -40\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"reason\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"4 skills matched | AI score: 40\",\n          \"0 skills matched | AI score: 0\",\n          \"2 skills matched | AI score: 20\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    }
  ]
}