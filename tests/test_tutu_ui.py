


def test_valid_authorization(authorization, email, password):
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email(email)
    authorization.login_with_password()
    authorization.fill_password(password)
    authorization.submit_authorization()
    authorization.open_menu()
    authorization.check_successful_authorization()

def test_logout(authorization, email, password):
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email(email)
    authorization.login_with_password()
    authorization.fill_password(password)
    authorization.submit_authorization()
    authorization.open_menu()
    authorization.check_successful_authorization()
    authorization.logout()
    authorization.check_logout()

def test_login_with_wrong_password(authorization, email, wr_pass):
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email(email)
    authorization.login_with_password()
    authorization.fill_password(wr_pass)
    authorization.submit_authorization()
    authorization.check_message_auth_error()

# def test_sorting_of_bus_tickets_by_lowest_price_first(tickets):
#     tickets.open()
#     tickets.bus_ticket()
#     tickets.set_route()