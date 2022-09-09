from django.shortcuts import redirect

from recruiter.views import global_recruiter_approval_checker

# main user role manager function for [admin, recruiter, candidate ]
def role_required_decorator(allowed_roles=[]):
    def decorator(view_fun):
        def wrap(request,*args, **kwargs):

            if request.user.extend_usermodel.role:
                # main check case
                if request.user.extend_usermodel.role in allowed_roles:
                    print('Permission ok')
                    return view_fun(request, *args, **kwargs)
                else:
                    print('Permission not ok')
                    print(request.user.extend_usermodel.role,'role')
                    return redirect('/')
            else:
                print('query not exist')
                print(request.user.extend_usermodel.role)
                return redirect('/')

        return wrap

    return decorator



def recruiter_permission_decorator(view_fun):
    def wrap(request,*args, **kwargs):

        if global_recruiter_approval_checker(request) == 'default' :
            print('default ok')

            return redirect('recruiter.dashboard')

        elif global_recruiter_approval_checker(request) == 'completed':
            print('completed ok')

            return redirect('recruiter.dashboard')

        elif global_recruiter_approval_checker(request) == 'deactive':
            print('deactivate ok')

            return redirect('recruiter.dashboard')

        else:
            print(' allowed ok')
            print(global_recruiter_approval_checker(request),'status')
            return view_fun(request, *args, **kwargs)

    return wrap
        