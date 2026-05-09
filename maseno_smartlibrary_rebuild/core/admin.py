from django.contrib import admin
from .models import Category, Book, BorrowRecord, Fine, SystemSettings, Profile, AuditLog


@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'library_name', 'school_email', 'school_phone', 'theme_color')
    search_fields = ('school_name', 'library_name', 'school_email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'admission_number', 'staff_number', 'phone', 'must_change_password')
    list_filter = ('role', 'must_change_password')
    search_fields = ('user__username', 'admission_number', 'staff_number', 'phone')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'total_copies', 'available_copies', 'status')
    list_filter = ('status', 'category')
    search_fields = ('title', 'author', 'isbn')


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'issue_date', 'due_date', 'return_date', 'returned')
    list_filter = ('returned', 'due_date', 'return_date')
    search_fields = ('book__title', 'user__username')


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('id', 'record', 'amount', 'paid', 'paid_date')
    list_filter = ('paid', 'paid_date')
    search_fields = ('record__user__username',)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'description', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('user__username', 'description')
    readonly_fields = ('user', 'action', 'description', 'created_at')