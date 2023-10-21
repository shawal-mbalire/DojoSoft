class UserQueryMixin():
    user_field = 'user'
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)