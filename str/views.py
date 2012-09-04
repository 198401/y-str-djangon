#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from str.forms import SearchForm
from models import STR
import random
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        f = SearchForm(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            if not cd['str1'] and not cd['str2'] \
               and not cd['str3'] and not cd['str4'] \
               and not cd['str5'] and not cd['str6'] \
               and not cd['str7'] and not cd['str8'] \
               and not cd['str9'] and not cd['str10'] \
               and not cd['str11'] and not cd['str12'] \
               and not cd['str13'] and not cd['str14'] \
               and not cd['str15'] and not cd['str16'] \
	       and not cd['str17'] and not cd['str18'] \
	       and not cd['str19'] and not cd['str20'] \
	       and not cd['str21'] and not cd['str22'] \
	       and not cd['str23'] and not cd['str24'] \
	       and not cd['str37'] \
            and not cd['str38']:
                error = u'未输入搜索条件'
                return render_to_response('base.html', locals())
            else:
                ssq = STR.objects.get_query_set()
                a=[]
		b=[]
		result=[]
                if cd['str1'] :
                    ssq = ssq.filter(str1__gte = 0)
		    a.append(int(cd['str1']))
		    b.append('str1')
		if cd['str2'] :
                    ssq = ssq.filter(str2__gte = 0)
		    a.append(int(cd['str2']))
		    b.append('str2')
		if cd['str3'] :
                    ssq = ssq.filter(str3__gte = 0)
                    a.append(int(cd['str3']))
                    b.append('str3')
                if cd['str4'] :
		    ssq = ssq.filter(str4__gte = 0)
		    a.append(int(cd['str4']))
		    b.append('str4')
		if cd['str5'] :
                    ssq = ssq.filter(str5__gte = 0)
		    a.append(int(cd['str5']))
		    b.append('str5')
		if cd['str6'] :
                    ssq = ssq.filter(str6__gte = 0)
		    a.append(int(cd['str6']))
		    b.append('str6')
		if cd['str7'] :
                    ssq = ssq.filter(str7__gte = 0)
		    a.append(int(cd['str7']))
		    b.append('str7')
		if cd['str8'] :
                    ssq = ssq.filter(str8__gte = 0)
		    a.append(int(cd['str8']))
		    b.append('str8')
		if cd['str9'] :
                    ssq = ssq.filter(str9__gte = 0)
                    a.append(int(cd['str9']))
                    b.append('str9')
		if cd['str10'] :
                    ssq = ssq.filter(str10__gte = 0)
		    a.append(int(cd['str10']))
		    b.append('str10')
		if cd['str11'] :
                    ssq = ssq.filter(str11__gte = 0)
		    a.append(int(cd['str11']))
		    b.append('str11')
		if cd['str12'] :
                    ssq = ssq.filter(str12__gte = 0)
                    a.append(int(cd['str12']))
                    b.append('str12')
		if cd['str13'] :
                    ssq = ssq.filter(str13__gte = 0)
		    a.append(int(cd['str13']))
		    b.append('str13')
		if cd['str14'] :
                    ssq = ssq.filter(str14__gte = 0)
		    a.append(int(cd['str14']))
		    b.append('str14')
		if cd['str15'] :
                    ssq = ssq.filter(str15__gte = 0)
                    a.append(int(cd['str15']))
                    b.append('str15')
		if cd['str16'] :
                    ssq = ssq.filter(str16__gte = 0)
		    a.append(int(cd['str16']))
		    b.append('str16')
		if cd['str17'] :
                    ssq = ssq.filter(str17__gte = 0)
		    a.append(int(cd['str17']))
		    b.append('str17')
		if cd['str18'] :
                    ssq = ssq.filter(str18__gte = 0)
                    a.append(int(cd['str18']))
                    b.append('str18')
		if cd['str19'] :
                    ssq = ssq.filter(str19__gte = 0)
		    a.append(int(cd['str19']))
		    b.append('str19')
		if cd['str20'] :
                    ssq = ssq.filter(str20__gte = 0)
		    a.append(int(cd['str20']))
		    b.append('str20')
		if cd['str21'] :
                    ssq = ssq.filter(str21__gte = 0)
                    a.append(int(cd['str21']))
                    b.append('str21')
		if cd['str22'] :
                    ssq = ssq.filter(str22__gte = 0)
		    a.append(int(cd['str22']))
		    b.append('str22')
		if cd['str23'] :
                    ssq = ssq.filter(str23__gte = 0)
		    a.append(int(cd['str23']))
		    b.append('str23')
		if cd['str24'] :
                    ssq = ssq.filter(str24__gte = 0)
                    a.append(int(cd['str24']))
                    b.append('str34')
		if cd['str37'] :
                    ssq = ssq.filter(str37__gte = 0)
		    a.append(int(cd['str37']))
		    b.append('str37')
		if cd['str38'] :
                    ssq = ssq.filter(str38__gte = 0)
                    a.append(int(cd['str38']))
                    b.append('str38')
		b.append('steps')
		result=[]
		for row in ssq:
		    sum=0
		    i=0
		    wd=[]
		    wd.append(row.id)
		    wd.append(row.ref)
		    wd.append(row.Population)
		    wd.append(row.location)
		    wd.append(row.SNP)
		    wd.append(row.HG)
		    if 'str1' in b:
			    wd.append(row.str1)
			    sum+=abs(row.str1-a[i])
			    i+=1
		    if 'str2' in b:
			    wd.append(row.str2)
			    sum+=abs(row.str2-a[i])
			    i+=1
		    if 'str3' in b:
			    wd.append(row.str3)
			    sum+=abs(row.str3-a[i])
			    i+=1
		    if 'str4' in b:
			    wd.append(row.str4)
			    sum+=abs(row.str4-a[i])
			    i+=1
		    if 'str5' in b:
			    wd.append(row.str5)
			    sum+=abs(row.str5-a[i])
			    i+=1
		    if 'str6' in b:
			    wd.append(row.str6)
			    sum+=abs(row.str6-a[i])
			    i+=1
		    if 'str7' in b:
			    wd.append(row.str7)
			    sum+=abs(row.str7-a[i])
			    i+=1
		    if 'str8' in b:
			    wd.append(row.str8)
			    sum+=abs(row.str8-a[i])
			    i+=1
		    if 'str9' in b:
			    wd.append(row.str9)
			    sum+=abs(row.str9-a[i])
			    i+=1
		    if 'str10' in b:
			    wd.append(row.str10)
			    sum+=abs(row.str10-a[i])
			    i+=1
		    if 'str11' in b:
			    wd.append(row.str11)
			    sum+=abs(row.str11-a[i])
			    i+=1
		    if 'str12' in b:
			    wd.append(row.str12)
			    sum+=abs(row.str12-a[i])
			    i+=1
		    if 'str13' in b:
			    wd.append(row.str13)
			    sum+=abs(row.str13-a[i])
			    i+=1
		    if 'str14' in b:
			    wd.append(row.str14)
			    sum+=abs(row.str14-a[i])
			    i+=1
		    if 'str15' in b:
			    wd.append(row.str15)
			    sum+=abs(row.str15-a[i])
			    i+=1
		    if 'str16' in b:
			    wd.append(row.str16)
			    sum+=abs(row.str16-a[i])
			    i+=1
		    if 'str17' in b:
			    wd.append(row.str17)
			    sum+=abs(row.str17-a[i])
			    i+=1
		    if 'str18' in b:
			    wd.append(row.str18)
			    sum+=abs(row.str18-a[i])
			    i+=1
		    if 'str19' in b:
			    wd.append(row.str19)
			    sum+=abs(row.str19-a[i])
			    i+=1
		    if 'str20' in b:
			    wd.append(row.str20)
			    sum+=abs(row.str20-a[i])
			    i+=1
		    if 'str21' in b:
			    wd.append(row.str21)
			    sum+=abs(row.str21-a[i])
			    i+=1
		    if 'str22' in b:
			    wd.append(row.str22)
			    sum+=abs(row.str22-a[i])
			    i+=1
		    if 'str23' in b:
			    wd.append(row.str23)
			    sum+=abs(row.str23-a[i])
			    i+=1
		    if 'str24' in b:
			    wd.append(row.str24)
			    sum+=abs(row.str24-a[i])
			    i+=1
		    if 'str37' in b:
			    wd.append(row.str37)
			    sum+=abs(row.str37-a[i])
			    i+=1
		    if 'str38' in b:
			    wd.append(row.str38)
			    sum+=abs(row.str38-a[i])
			    i+=1
		    if sum<6:
                            wd.append(sum)                         
			    result.append(wd)
		    
		result.sort(key=lambda x:x[-1])
		if len(result)>50:
			xx=result[:50]
		else:
			xx=result
		xxx=['id','ref','Population','location','SNP','HG']+b

                return render_to_response('base.html',  {'ty':xxx,'ystr': xx})
        else:
            error = u'输入条件错误'
            return render_to_response('base.html', locals())
    else:
        f = SearchForm()
        return render_to_response('base.html', locals())
