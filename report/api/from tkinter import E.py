from tkinter import E

 
# def create_case(request):
#     user = request.usere}

#     if request.method == "POST":
#         about = request.POST["about"]
#         salary = request.POST["salary"]

#         obj = Case(
#             fkdfdjhfdfd
#         )

#         obj.save()

#         selected_tech = []
#         for t in range(0, 10):
#             try:
#                 name = request.POST[f"victim_name_{t}"]
#                 address = request.POST[f"victim_address_{t}"] 

#                 victim = Victim(
#                     case = obj,
#                     name = name
#                 )
#                 victim.save()
            
#             except Exception as e:
#                 print(str(e))
#         User.objects.filter(id=user.id).update(
#             about=about, salary=salary)
#         profile = User.objects.get(id=user.id)
#         for item in selected_tech:
#             profile.tech.add(Tech.objects.get(pk=item))
#         return redirect('socials')
#     else:
#         return render(
#             request, "users/pages/about_tech_update.html", context
#         )