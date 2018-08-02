
class AdminPageLocators(object):
    # admin login page locators
    admin_signIn_userName = 'id_username'
    admin_signIn_password = 'id_password'
    admin_signIn_button = "//input[@value='Log in']"


class GroupPageLocators(object):
    # admin page groups locators
    press_groups_link = "Groups"
    add_group_link = "ADD GROUP"
    search_group = 'searchbar'
    bt_search = "/html/body/div/div[3]/div/div/div/form/div/input[2]"
    group_name = 'id_name'
    group_permissions = 'id_permissions_add_all_link'
    save_group = "//input[@value='Save']"
    group_check_box = 'action-checkbox'
    group_exists = '/html/body/div/div[3]/div/form/div/fieldset/div[1]/ul/li'
    select_action = '/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]'
    press_bt_go = '.button'
    press_bt_confirm = '#content > form:nth-child(7) > div:nth-child(2) > ''input:nth-child(4)'


class UserPageLocators(object):
    # user page locators
    press_users_link = "Users"
    press_add_user_link = "ADD USER"
    username = 'id_username'
    user_password = 'id_password1'
    user_confirm_password = 'id_password2'
    add_new_user_bt = '.default'
    user_first_name = 'id_first_name'
    user_last_name = 'id_last_name'
    user_email = 'id_email'
    user_permissions = 'id_user_permissions_add_all_link'
    select_check_box = '/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td[1]/input'
    select_delete_option = '/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]'
    bt_go = '.button'
    confirm_delete = '#content > form:nth-child(7) > div:nth-child(2) > input:nth-child(4)'


class AuthorsPageLocators(object):
    # admin page authors locator
    press_authors_link = "Authors"
    press_add_author = "ADD AUTHOR"
    authors_first_name = 'id_first_name'
    authors_last_name = 'id_last_name'
    authors_birth_date = 'id_date_of_birth'
    authors_death_date = 'id_date_of_death'
    # adding a book locators within authors page
    add_book_title = 'id_book_set-0-title'
    add_book_summary = 'id_book_set-0-summary'
    add_book_isbn = 'id_book_set-0-isbn'
    add_book_genre = '/html/body/div[1]/div[3]/div/form/div/div[1]/div/''fieldset/table/tbody/tr[1]/td[5]/div/select/option'
    add_book_language = '/html/body/div[1]/div[3]/div/form/div/div[1]/div/fieldset/''table/tbody/tr[1]/td[6]/div/select/option[2]'
    save_author_and_book = '.default'
    select_delete_author = '/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[3]/td[1]/input'
    select_delete = '/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]'
    bt_go = '.button'
    confirm_delete = '/html/body/div/div[3]/form/div/input[4]'


class BookInstancesLocators(object):
    # book instances locators
    press_book_instance_link = 'Book instances'
    press_add_book_instance = 'ADD BOOK INSTANCE'
    select_book = '/html/body/div[1]/div[3]/div/form/div/fieldset[1]/div[1]/div/div/select/option[2]'
    book_imprint = 'id_imprint'
    book_status = 'id_status'
    book_due = 'id_status'
    book_borrower = 'id_borrower'
    save_instance = '.default'


class BookPageLocators(object):
    # book page locators
    press_books_link = "Books"
    press_add_book = "ADD BOOK"
    book_title = 'id_title'
    book_author = 'id_author'
    book_summary = 'id_summary'
    book_isbn = 'id_isbn'
    book_genre = 'id_genre'
    book_language = 'id_language'
    save_book = '.default'


class GenresPageLocators(object):
    press_genres_link = 'Genres'
    press_add_genre_link = 'ADD GENRE'
    fill_genre = 'id_name'
    save_genre = '.default'


class LanguagesPageLocators(object):
    press_language_link = 'Languages'
    press_add_language = 'ADD LANGUAGE'
    fill_in_language = 'id_name'
    save_language = '.default'




