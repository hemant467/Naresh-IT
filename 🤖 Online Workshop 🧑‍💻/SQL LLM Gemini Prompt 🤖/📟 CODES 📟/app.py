import streamlit as st
import sqlite3
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_key)  # Replace with your actual API key

# Function: Prompt Gemini to generate SQL
def get_gemini_sql(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "")
    return sql_query

# Function: Optional SQL explanation
def explain_sql_query(query):
    explain_prompt = f"Explain this SQL query step-by-step in simple terms:\n{query}"
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(explain_prompt)
    return response.text.strip()

# Function: Run SQL on SQLite and return rows + column names
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]  # dynamic column names
        conn.close()
        return rows, col_names
    except sqlite3.Error as e:
        return [("SQL Error", str(e))], ["Error"]

# Professional 6-Part Prompt for Gemini
prompt = ["""
# 1. Context:
You are helping a user interact with a SQLite database using natural language.

# 2. Role:
You are an expert SQL assistant who converts English questions into SQLite queries.

# 3. Constraints:
- Use only SQLite syntax.
- Target database: Naresh_it_employee1.
- Table: Naresh_it_employee1.
- Columns: employee_name (text), employee_role (text), employee_salary (float).
- Do not use backticks (`), triple quotes (```), or semicolons.
- Keep SQL readable and correct.

# 4. Instructions:
- Translate the user's question into a valid SQL query.
- Be precise in filtering, grouping, or sorting.
- Make sure the column names and logic match the schema.

# 5. Few-shot Examples:

Q: How many employees are there?
A: SELECT COUNT(*) FROM Naresh_it_employee1

Q: Show all Data Engineers
A: SELECT * FROM Naresh_it_employee1 WHERE employee_role = 'Data Engineer'

Q: Who earns more than 60000?
A: SELECT * FROM Naresh_it_employee1 WHERE employee_salary > 60000

Q: Who earns the highest salary?
A: SELECT * FROM Naresh_it_employee1 ORDER BY employee_salary DESC LIMIT 1

# 6. Chain of Thought:
First, understand the user’s question and identify relevant filters or conditions.  
Then map to the appropriate SQL clause (e.g., SELECT, WHERE, GROUP BY, ORDER BY).  
Finally, return the correct and clean SQL query.

Now generate the SQL query for this question:
"""]

# Streamlit App UI
st.set_page_config(page_title="LLM SQL Assistant")
st.title("Gemini SQL Assistant (Naresh IT DB)")
st.write("Ask questions in English. Get SQL queries and results instantly!")

# User input
question = st.text_input("Enter your question:")

# Sample suggestions
with st.expander("Try These Examples"):
    st.markdown("""
    - List all employees.
    - Show only Data Scientists.
    - Who earns more than 60,000?
    - Count of Data Engineers?
    - Highest salary employee?
    - Provide the average salary based on job role.
    """)

# Submit
if st.button("Run"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Generate SQL
        sql_query = get_gemini_sql(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")

        # Run SQL query
        result, columns = read_sql_query(sql_query, "Naresh_it_employee1.db")

        # Show result
        if result and "SQL Error" in result[0]:
            st.error(f"Error: {result[0][1]}")
        else:
            st.subheader("Query Result:")
            df = pd.DataFrame(result, columns=columns)
            st.dataframe(df, use_container_width=True)

            # Explanation
            with st.expander("Gemini Explains the SQL"):
                explanation = explain_sql_query(sql_query)
                st.write(explanation)
