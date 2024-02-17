from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, TemplateView
from .models import BanBan
from .forms import PhotoUploadForm

# Create your views here.
class PhotosView(TemplateView):
    template_name = "photos/photos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banban = BanBan.objects.first()
        context["photo_dict"] = {
            "banban": banban
        }
        return context
    


class BanBanView(View):
    # template_name = "photos/single_photo.html"
    # model = BanBan
    # context_object_name = "single"
    def get(self, request, pk):
        current_image = BanBan.objects.filter(pk=pk)[0]
        image_id_list = [x.id for x in list(BanBan.objects.all())]
        prev_id = image_id_list[image_id_list.index(pk) - 1] if image_id_list.index(pk) - 1 >= 0 else -1
        next_id = image_id_list[image_id_list.index(pk) + 1] if image_id_list.index(pk) + 1 < len(image_id_list) else -1
        
        upload_form = PhotoUploadForm()
        return render(request, "photos/single_photo.html", {
            "single": current_image,
            "prev_id": prev_id,
            "next_id": next_id,
            "image_id_list": image_id_list,
            "form": upload_form,
        })

    def post(self, request, pk):
        current_image = BanBan.objects.filter(pk=pk)[0]
        submitted_form = PhotoUploadForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            photo = BanBan(image=request.FILES["image"])
            photo.save()
            return HttpResponseRedirect(reverse("banban", args=[pk]))
        
        return render(request, "photos/single_photo.html", {
            "single": current_image,
            "form": submitted_form
        })