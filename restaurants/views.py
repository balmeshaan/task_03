from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    		{
    			'restaurant_name':'food inc',
    			'food_type':'general'
    		},
    		{
    			'restaurant_name':'banana republic',
    			'food_type':'vegan'
    		},
    		{
    			'restaurant_name':'meat',
    			'food_type':'carnivore diet'
    		}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': 
			{	
				'restaurant_name':'meat',
				'food_type':'carnivore diet'
			}
    	
    }
    return render(request, 'detail.html', context)
