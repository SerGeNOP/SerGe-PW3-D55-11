from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, LendedBooks


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'publisher')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(LendedBooks)
class LendedBooksAdmin(admin.ModelAdmin):
    list_display = ('friend', 'book', 'date_lend_in', 'date_lend_out')

