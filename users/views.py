from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ShopDetailsForm
from users import charts
from .apps import UsersConfig
from keras.preprocessing import image
import numpy as np
import os 

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('users:dashboard')
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('users:dashboard')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'app/signup.html', {'form': form})


@login_required
def dashboard_view(request):
	context = {
        'time_series_chart': charts.TimeSeriesChart(),
        'scatter_line_chart': charts.ScatterLineChart(),
        'bar_chart': charts.BarChart(),
        'radar_chart': charts.RadarChart(),
        'polar_chart': charts.PolarChart(),
        'pie_chart': charts.PieChart(),
        'bubble_chart': charts.BubbleChart(),
    }
    # data = defaultdict(lambda:0)
	# line_data = defaultdict(list)
	# values = []
	# shopnames = list(set(df['ShopName']))
	# for ind in df.index:
	# 	line_data[df['ShopName'][ind]].append(df['Quantity'][ind])
	# 	data[df['ShopName'][ind]]+=df['Quantity'][ind]
	# n = 0
	# for i in line_data:
	# 	n = max(n,len(line_data[i]))
	# for i in line_data:
	# 	line_data[i] = line_data[i]+[0]*(n-len(line_data[i]))
	# print(line_data)
	# for i in shopnames:
	# 	values.append(data[i])
	# pie_data = []
	# for i in data:
	# 	temp = {}
	# 	temp['name'] = i
	# 	temp['y'] = data[i]
	# 	pie_data.append(temp)
	# pie_data[0]['sliced'] = 1
	# pie_data[0]['selected'] = 1
	# line_chart = []
	# for i in line_data:
	# 	temp = {}
	# 	temp['name'] = i
	# 	temp['data'] = line_data[i]
	# 	line_chart.append(temp)
	# content = {'pie_data':pie_data,'values':values,'line_chart':line_chart}
	# print(line_chart)
	return render(request, 'app/dashboard.html',context)

def rewards_view(request):
	return render(request, 'app/rewards.html')

def home_view(request):
	return render(request, 'app/home.html')

def shop_details_view(request):
	form = ShopDetailsForm()
	return render(request,'app/shop_details.html',{'form':form})

def sastakaam(request):
	model = UsersConfig.MODEL
	img_path = os.path.join(os.path.dirname(UsersConfig.BASE_PATH), 'something.png')
	img = image.load_img(img_path, target_size=(300, 300))
	img = image.img_to_array(img, dtype=np.uint8)
	img=np.array(img)/255.0
	p = model.predict(img[np.newaxis, ...])
	x = np.max(p[0], axis=-1) 
	print("Maximum Probability: ", x)
	# predicted_class = labels[np.argmax(p[0], axis=-1)]
	# print("Classified:",predicted_class)
	return render(request, 'app/mlscript.html', {'paisa': x})