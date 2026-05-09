from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    login_view,
    logout_view,
    dashboard,
    change_password,

    # BOOKS
    book_list,
    add_book,
    edit_book,
    delete_book,
    issue_book,

    # QR CODES
    book_qr_code,
    book_qr_print,

    # BORROW RECORDS
    borrow_records,
    return_book,
    mark_fine_paid,
    export_borrow_records_excel,
    borrow_receipt_pdf,

    # USERS
    add_user,
    user_list,
    edit_user,
    delete_user,

    # BULK UPLOAD
    bulk_upload_students,

    # PASSWORD RESET
    reset_student_password,

    # AUDIT LOGS
    audit_logs,
)

urlpatterns = [

    # HOME
    path('', home, name='home'),

    # AUTH
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('change-password/', change_password, name='change_password'),

    # BOOK MANAGEMENT
    path('books/', book_list, name='book_list'),

    path(
        'books/add/',
        add_book,
        name='add_book'
    ),

    path(
        'books/edit/<int:book_id>/',
        edit_book,
        name='edit_book'
    ),

    path(
        'books/delete/<int:book_id>/',
        delete_book,
        name='delete_book'
    ),

    path(
        'books/issue/<int:book_id>/',
        issue_book,
        name='issue_book'
    ),

    # QR CODE ROUTES
    path(
        'books/<int:book_id>/qr/',
        book_qr_code,
        name='book_qr_code'
    ),

    path(
        'books/<int:book_id>/qr-print/',
        book_qr_print,
        name='book_qr_print'
    ),

    # BORROW RECORDS
    path(
        'borrow-records/',
        borrow_records,
        name='borrow_records'
    ),

    path(
        'borrow-records/export/excel/',
        export_borrow_records_excel,
        name='export_borrow_records_excel'
    ),

    path(
        'borrow-records/<int:record_id>/receipt/',
        borrow_receipt_pdf,
        name='borrow_receipt_pdf'
    ),

    path(
        'return-book/<int:record_id>/',
        return_book,
        name='return_book'
    ),

    path(
        'fine-paid/<int:fine_id>/',
        mark_fine_paid,
        name='mark_fine_paid'
    ),

    # USER MANAGEMENT
    path(
        'add-user/',
        add_user,
        name='add_user'
    ),

    path(
        'users/',
        user_list,
        name='user_list'
    ),

    path(
        'users/edit/<int:profile_id>/',
        edit_user,
        name='edit_user'
    ),

    path(
        'users/delete/<int:profile_id>/',
        delete_user,
        name='delete_user'
    ),

    # BULK UPLOAD
    path(
        'bulk-upload-students/',
        bulk_upload_students,
        name='bulk_upload_students'
    ),

    # PASSWORD RESET
    path(
        'reset-student-password/',
        reset_student_password,
        name='reset_student_password'
    ),

    # AUDIT LOGS
    path(
        'audit-logs/',
        audit_logs,
        name='audit_logs'
    ),

    # DJANGO ADMIN
    path(
        'admin/',
        admin.site.urls
    ),
]