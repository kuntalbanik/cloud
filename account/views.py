# # from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth.models import User
# from django.views.generic import UpdateView

# from .forms import UserProfileForm

# class UserProfileUpdateView(UpdateView):
#     model = User
    
#     def get_initial(self):
#         initial = super(UserProfileUpdateView, self).get_initial()
#         try:
#             current_group = self.object.groups.get()
#         except:
#             # exception can occur if the edited user has no groups
#             # or has more than one group
#             pass
#         else:
#             initial['group'] = current_group.pk
#         return initial
    
#     def get_form_class(self):
#         return UserProfileForm
    
#     def form_valid(self, form):
#         self.object.groups.clear()
#         self.object.groups.add(form.cleaned_data['group'])
#         return super(UserProfileUpdateView, self).form_valid(form)