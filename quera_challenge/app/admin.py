from django.contrib import admin
from .models import User
from .models import Award, AwardTransaction
from .models import Challenge, ChallengeTransaction, ChallengeItem

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')  # Customize fields as necessary
    search_fields = ('username', 'email')

# Register the Award model
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Customize fields as necessary
    search_fields = ('name',)

# Register the AwardTransaction model
@admin.register(AwardTransaction)
class AwardTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'award', )  # Customize fields as necessary
    search_fields = ('user__username', 'award__name')

# Register the Challenge model
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Customize fields as necessary
    search_fields = ('title',)

# Register the ChallengeTransaction model
@admin.register(ChallengeTransaction)
class ChallengeTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', )  # Customize fields as necessary
    search_fields = ('user__username', 'challenge__title')

# Register the ChallengeItem model
@admin.register(ChallengeItem)
class ChallengeItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_to_display')  # Customize fields as necessary
    search_fields = ('title',)
