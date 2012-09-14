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
            if not cd['DYS388'] and not cd['DYS19'] \
               and not cd['DYS389I'] and not cd['DYS389II'] \
               and not cd['DYS390'] and not cd['DYS391'] \
               and not cd['DYS392'] and not cd['DYS393'] \
               and not cd['DYS425'] and not cd['DYS426'] \
               and not cd['DYS434'] and not cd['DYS435'] \
               and not cd['DYS436'] and not cd['DYS437'] \
               and not cd['DYS438'] and not cd['DYS439'] \
	       and not cd['DYS385a'] and not cd['DYS385b'] \
	       and not cd['DYSA1_2'] and not cd['YGATAH4'] \
	       and not cd['DYS448'] and not cd['DYS456'] \
	       and not cd['DYS458'] and not cd['DYS635'] \
	       and not cd['YCAIIa'] and not cd['YCAIIb'] \
	       and not cd['DYS594'] and not cd['DYS596'] \
	       and not cd['DYSA1_2'] and not cd['YGATAH4'] \
	       and not cd['YPENTA1'] and not cd['YPENTA2'] \
	       and not cd['DYS643'] and not cd['DYS645'] \
	       and not cd['DYF411S1a'] \
            and not cd['DYF411S1b']:
                error = u'未输入搜索条件'
                return render_to_response('base.html', locals())
            else:
                ssq = STR.objects.get_query_set()
                a=[]
		b=[]
		result=[]
                if cd['DYS388'] :
                    ssq = ssq.filter(DYS388__gte = 0)
		    a.append(int(cd['DYS388']))
		    b.append('DYS388')
		if cd['DYS19'] :
                    ssq = ssq.filter(DYS19__gte = 0)
		    a.append(int(cd['DYS19']))
		    b.append('DYS19')
		if cd['DYS389I'] :
                    ssq = ssq.filter(DYS389I__gte = 0)
                    a.append(int(cd['DYS389I']))
                    b.append('DYS389I')
                if cd['DYS389II'] :
		    ssq = ssq.filter(DYS389II__gte = 0)
		    a.append(int(cd['DYS389II']))
		    b.append('DYS389II')
		if cd['DYS390'] :
                    ssq = ssq.filter(DYS390__gte = 0)
		    a.append(int(cd['DYS390']))
		    b.append('DYS390')
		if cd['DYS391'] :
                    ssq = ssq.filter(DYS391__gte = 0)
		    a.append(int(cd['DYS391']))
		    b.append('DYS391')
		if cd['DYS392'] :
                    ssq = ssq.filter(DYS392__gte = 0)
		    a.append(int(cd['DYS392']))
		    b.append('DYS392')
		if cd['DYS393'] :
                    ssq = ssq.filter(DYS393__gte = 0)
		    a.append(int(cd['DYS393']))
		    b.append('DYS393')
		if cd['DYS425'] :
                    ssq = ssq.filter(DYS425__gte = 0)
                    a.append(int(cd['DYS425']))
                    b.append('DYS425')
		if cd['DYS426'] :
                    ssq = ssq.filter(DYS426__gte = 0)
		    a.append(int(cd['DYS426']))
		    b.append('DYS426')
		if cd['DYS434'] :
                    ssq = ssq.filter(DYS434__gte = 0)
		    a.append(int(cd['DYS434']))
		    b.append('DYS434')
		if cd['DYS435'] :
                    ssq = ssq.filter(DYS435__gte = 0)
                    a.append(int(cd['DYS435']))
                    b.append('DYS435')
		if cd['DYS436'] :
                    ssq = ssq.filter(DYS436__gte = 0)
		    a.append(int(cd['DYS436']))
		    b.append('DYS436')
		if cd['DYS437'] :
                    ssq = ssq.filter(DYS437__gte = 0)
		    a.append(int(cd['DYS437']))
		    b.append('DYS437')
		if cd['DYS438'] :
                    ssq = ssq.filter(DYS438__gte = 0)
                    a.append(int(cd['DYS438']))
                    b.append('DYS438')
		if cd['DYS439'] :
                    ssq = ssq.filter(DYS439__gte = 0)
		    a.append(int(cd['DYS439']))
		    b.append('DYS439')
		if cd['DYS385a'] :
                    ssq = ssq.filter(DYS385a__gte = 0)
		    a.append(int(cd['DYS385a']))
		    b.append('DYS385a')
		if cd['DYS385b'] :
                    ssq = ssq.filter(DYS385b__gte = 0)
                    a.append(int(cd['DYS385b']))
                    b.append('DYS385b')
		if cd['DYSA1_2'] :
                    ssq = ssq.filter(DYSA1_2__gte = 0)
		    a.append(int(cd['DYSA1_2']))
		    b.append('DYSA1_2')
		if cd['YGATAH4'] :
                    ssq = ssq.filter(YGATAH4__gte = 0)
		    a.append(int(cd['YGATAH4']))
		    b.append('YGATAH4')
		if cd['DYS448'] :
                    ssq = ssq.filter(DYS448__gte = 0)
                    a.append(int(cd['DYS448']))
                    b.append('DYS448')
		if cd['DYS456'] :
                    ssq = ssq.filter(DYS456__gte = 0)
		    a.append(int(cd['DYS456']))
		    b.append('DYS456')
		if cd['DYS458'] :
                    ssq = ssq.filter(DYS458__gte = 0)
		    a.append(int(cd['DYS458']))
		    b.append('DYS458')
		if cd['DYS635'] :
                    ssq = ssq.filter(DYS635__gte = 0)
                    a.append(int(cd['DYS635']))
                    b.append('DYS635')
		if cd['YCAIIa'] :
                    ssq = ssq.filter(YCAIIa__gte = 0)
		    a.append(int(cd['YCAIIa']))
		    b.append('YCAIIa')
		if cd['YCAIIb'] :
                    ssq = ssq.filter(YCAIIb__gte = 0)
                    a.append(int(cd['YCAIIb']))
                    b.append('YCAIIb')
                if cd['DYS594'] :
                    ssq = ssq.filter(DYS594__gte = 0)
                    a.append(int(cd['DYS594']))
                    b.append('DYS594')
                if cd['DYS596'] :
                    ssq = ssq.filter(DYS596__gte = 0)
                    a.append(int(cd['DYS596']))
                    b.append('DYS596')
                if cd['YPENTA1'] :
                    ssq = ssq.filter(YPENTA1__gte = 0)
                    a.append(int(cd['YPENTA1']))
                    b.append('YPENTA1')
                if cd['YPENTA2'] :
                    ssq = ssq.filter(YPENTA2__gte = 0)
                    a.append(int(cd['YPENTA2']))
                    b.append('YPENTA2')
                if cd['DYS643'] :
                    ssq = ssq.filter(DYS643__gte = 0)
                    a.append(int(cd['DYS643']))
                    b.append('DYS643')
                if cd['DYS645'] :
                    ssq = ssq.filter(DYS645__gte = 0)
                    a.append(int(cd['DYS645']))
                    b.append('DYS645')
                if cd['DYF411S1a'] :
                    ssq = ssq.filter(DYF411S1a__gte = 0)
                    a.append(int(cd['DYF411S1a']))
                    b.append('DYF411S1a')
                if cd['DYF411S1b'] :
                    ssq = ssq.filter(DYF411S1b__gte = 0)
                    a.append(int(cd['DYF411S1b']))
                    b.append('DYF411S1b')
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
		    if 'DYS388' in b:
			    wd.append(row.DYS388)
			    sum+=abs(row.DYS388-a[i])
			    i+=1
		    if 'DYS19' in b:
			    wd.append(row.DYS19)
			    sum+=abs(row.DYS19-a[i])
			    i+=1
		    if 'DYS389I' in b:
			    wd.append(row.DYS389I)
			    sum+=abs(row.DYS389I-a[i])
			    i+=1
		    if 'DYS389II' in b:
			    wd.append(row.DYS389II)
			    sum+=abs(row.DYS389II-a[i])
			    i+=1
		    if 'DYS390' in b:
			    wd.append(row.DYS390)
			    sum+=abs(row.DYS390-a[i])
			    i+=1
		    if 'DYS391' in b:
			    wd.append(row.DYS391)
			    sum+=abs(row.DYS391-a[i])
			    i+=1
		    if 'DYS392' in b:
			    wd.append(row.DYS392)
			    sum+=abs(row.DYS392-a[i])
			    i+=1
		    if 'DYS393' in b:
			    wd.append(row.DYS393)
			    sum+=abs(row.DYS393-a[i])
			    i+=1
		    if 'DYS425' in b:
			    wd.append(row.DYS425)
			    sum+=abs(row.DYS425-a[i])
			    i+=1
		    if 'DYS426' in b:
			    wd.append(row.DYS426)
			    sum+=abs(row.DYS426-a[i])
			    i+=1
		    if 'DYS434' in b:
			    wd.append(row.DYS434)
			    sum+=abs(row.DYS434-a[i])
			    i+=1
		    if 'DYS435' in b:
			    wd.append(row.DYS435)
			    sum+=abs(row.DYS435-a[i])
			    i+=1
		    if 'DYS436' in b:
			    wd.append(row.DYS436)
			    sum+=abs(row.DYS436-a[i])
			    i+=1
		    if 'DYS437' in b:
			    wd.append(row.DYS437)
			    sum+=abs(row.DYS437-a[i])
			    i+=1
		    if 'DYS438' in b:
			    wd.append(row.DYS438)
			    sum+=abs(row.DYS438-a[i])
			    i+=1
		    if 'DYS439' in b:
			    wd.append(row.DYS439)
			    sum+=abs(row.DYS439-a[i])
			    i+=1
		    if 'DYS385a' in b:
			    wd.append(row.DYS385a)
			    sum+=abs(row.DYS385a-a[i])
			    i+=1
		    if 'DYS385b' in b:
			    wd.append(row.DYS385b)
			    sum+=abs(row.DYS385b-a[i])
			    i+=1
		    if 'DYSA1_2' in b:
			    wd.append(row.DYSA1_2)
			    sum+=abs(row.DYSA1_2-a[i])
			    i+=1
		    if 'YGATAH4' in b:
			    wd.append(row.YGATAH4)
			    sum+=abs(row.YGATAH4-a[i])
			    i+=1
		    if 'DYS448' in b:
			    wd.append(row.DYS448)
			    sum+=abs(row.DYS448-a[i])
			    i+=1
		    if 'DYS456' in b:
			    wd.append(row.DYS456)
			    sum+=abs(row.DYS456-a[i])
			    i+=1
		    if 'DYS458' in b:
			    wd.append(row.DYS458)
			    sum+=abs(row.DYS458-a[i])
			    i+=1
		    if 'DYS635' in b:
			    wd.append(row.DYS635)
			    sum+=abs(row.DYS635-a[i])
			    i+=1
		    if 'YCAIIa' in b:
			    wd.append(row.YCAIIa)
			    sum+=abs(row.YCAIIa-a[i])
			    i+=1
		    if 'YCAIIb' in b:
			    wd.append(row.YCAIIb)
			    sum+=abs(row.YCAIIb-a[i])
			    i+=1
		    if 'DYS594' in b:
			    wd.append(row.DYS594)
			    sum+=abs(row.DYS594-a[i])
			    i+=1
		    if 'DYS596' in b:
			    wd.append(row.DYS596)
			    sum+=abs(row.DYS596-a[i])
			    i+=1
		    if 'YPENTA1' in b:
			    wd.append(row.YPENTA1)
			    sum+=abs(row.YPENTA1-a[i])
			    i+=1
		    if 'YPENTA2' in b:
			    wd.append(row.YPENTA2)
			    sum+=abs(row.YPENTA2-a[i])
			    i+=1
		    if 'DYS643' in b:
			    wd.append(row.DYS643)
			    sum+=abs(row.DYS643-a[i])
			    i+=1
		    if 'DYS645' in b:
			    wd.append(row.DYS645)
			    sum+=abs(row.DYS645-a[i])
			    i+=1
		    if 'DYF411S1a' in b:
			    wd.append(row.DYF411S1a)
			    sum+=abs(row.DYF411S1a-a[i])
			    i+=1
		    if 'DYF411S1b' in b:
			    wd.append(row.DYF411S1b)
			    sum+=abs(row.DYF411S1b-a[i])
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
