import streamlit as st

# Sets the page title and page icon
st.set_page_config(page_title="FinancePro", page_icon=":money_with_wings:")

# Define functions for different pages
def homepage():
    st.write("<h1 style='text-align: center;'>Welcome to FinancePro!</h1>", unsafe_allow_html=True)

    # A brief description for my finance app
    st.write("<h6 style='text-align: center;'>This is your personal finance management tool. Get started by selecting an option from the sidebar.</h6>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # Adds an image to the homepage
    st.image("media/financepro.jpg")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("<h6 style='text-align: left;'>FinancePro is an easy-to-use financial planning tool that helps you manage your expenses and stay on top of your finances.</h6>", unsafe_allow_html=True)

    # Adds a list of features
    st.write("<h4 style='text-align: left;'>Key features:</h4>", unsafe_allow_html=True)
    st.write(
        "<ul style='text-align: left;'><li>Track your income and expenses</li><li>Create a budget and set financial goals</li><li>Visualize your spending habits with interactive charts and graphs</li></ul>",
        unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Adds a subscription form
    email_text = '<span style="font-size: 18px;">Like our website? Enter your email address to subscribe to our newsletter:</span>'
    st.markdown(email_text, unsafe_allow_html=True)
    email = st.text_input("", key="email", value="")
    if st.button("Subscribe"):
        st.success(f"Thank you for subscribing with email: {email}")


def budget_page():
    st.write("# Budget Planner")
    # Get user's monthly income
    monthly_income = st.slider("Enter your monthly income:", min_value=0, max_value=20000, step=1, format="$%.2f")

    # Get user's monthly expenses
    st.subheader("Monthly Expenses")

    # Get user's housing expenses
    housing_expenses = st.number_input("Housing:", min_value=0, value=0, step=100)

    # Get user's transportation expenses
    transportation_expenses = st.number_input("Transportation:", min_value=0, value=0, step=100)

    # Get user's food expenses
    food_expenses = st.number_input("Food:", min_value=0, value=0, step=100)

    # Get user's entertainment expenses
    entertainment_expenses = st.number_input("Entertainment:", min_value=0, value=0, step=100)

    # Get user's shopping expenses
    shopping_expenses = st.number_input("Shopping:", min_value=0, value=0, step=100)

    other_expenses = st.number_input("Other:", min_value=0, value=0, step=100)

    # Calculate total monthly expenses
    total_expenses = housing_expenses + transportation_expenses + food_expenses + entertainment_expenses + shopping_expenses + other_expenses

    # Calculate remaining budget
    remaining_budget = monthly_income - total_expenses

    # Display remaining budget to user
    st.subheader("Remaining Budget")
    st.write("Your remaining budget for this month is: $", remaining_budget, style={"font-size": "304px"})

def investments_page():
    st.write("# Investments")
    st.write("Please enter the following information about your investment:")

    investment_name = st.text_input("Investment Name:")
    investment_type = st.selectbox("Investment Type:", ["Stocks", "Bonds", "Mutual Funds"])
    investment_amount = st.number_input("Amount Invested ($):", min_value=0.0, step=100.0)
    investment_return = st.number_input("Expected Annual Return (%):", min_value=0.0, max_value=100.0, step=0.01)
    investment_term = st.number_input("Investment Term (years):", min_value=1, step=1)

    future_value = investment_amount * ((1 + investment_return / 100) ** investment_term)
    future_value = round(future_value, 2)

    st.write(
        f"The future value of your {investment_type.lower()} investment in {investment_term} year(s) is: ${future_value:.2f}")

def goals_page():
    st.write("# Financial Goals")
    current_savings = st.number_input("Current Savings", min_value=0.0, step=1.0)
    monthly_contribution = st.number_input("Monthly Contribution", min_value=0.0, step=1.0)
    time_horizon = st.number_input("Time Horizon (in years)", min_value=1, step=1)

    future_value = calculate_future_value(current_savings, monthly_contribution, time_horizon)

    st.write(
        f"Based on your inputs, your future value will be: <span style='font-size: 20px;'>${future_value:.2f}</span>",
        unsafe_allow_html=True)


def calculate_future_value(current_savings, monthly_contribution, time_horizon):
    interest_rate = 0.05  # example interest rate
    num_periods = time_horizon * 12
    future_value = current_savings * (1 + interest_rate / 12) ** num_periods
    future_value += monthly_contribution * (((1 + interest_rate / 12) ** num_periods - 1) / (interest_rate / 12))
    return future_value

# Defines the sidebar options
options = {
    "Home": homepage,
    "Budget Planner": budget_page,
    "Investments": investments_page,
    "Financial Goals": goals_page
}

# Creates the sidebar
selection = st.sidebar.radio("Select a page", list(options.keys()))

# Calls function for selected page
options[selection]()
