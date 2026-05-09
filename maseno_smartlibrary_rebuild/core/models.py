from django.db import models
from django.contrib.auth.models import User


class SystemSettings(models.Model):
    school_name = models.CharField(max_length=200, default="Maseno SmartLib")
    library_name = models.CharField(max_length=200, default="School Library")
    school_email = models.EmailField(blank=True, null=True)
    school_phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    theme_color = models.CharField(max_length=20, default="#0d6efd")

    class Meta:
        verbose_name = "System Setting"
        verbose_name_plural = "System Settings"

    def __str__(self):
        return self.school_name


class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('teacher', 'Teacher/Staff'),
        ('student', 'Student'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    admission_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )

    staff_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )

    phone = models.CharField(max_length=50, blank=True, null=True)

    must_change_password = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)

    isbn = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    publisher = models.CharField(max_length=150, blank=True)

    year_published = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.status = 'available' if self.available_copies > 0 else 'unavailable'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    return_date = models.DateField(
        blank=True,
        null=True
    )

    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class Fine(models.Model):
    record = models.OneToOneField(BorrowRecord, on_delete=models.CASCADE)

    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    paid = models.BooleanField(default=False)

    paid_date = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.record.user.username} - KES {self.amount}"


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('add_user', 'Add User'),
        ('edit_user', 'Edit User'),
        ('delete_user', 'Delete User'),
        ('bulk_upload', 'Bulk Upload'),
        ('add_book', 'Add Book'),
        ('edit_book', 'Edit Book'),
        ('delete_book', 'Delete Book'),
        ('issue_book', 'Issue Book'),
        ('return_book', 'Return Book'),
        ('fine_paid', 'Fine Paid'),
        ('password_reset', 'Password Reset'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        username = self.user.username if self.user else "System"
        return f"{username} - {self.action}"