from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm


def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserChangeForm()
    else:
        # 处理填写好的表单
        form = UserChangeForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重新定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)
# Create your views here.
