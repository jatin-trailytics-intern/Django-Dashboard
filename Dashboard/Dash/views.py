from django.shortcuts import render, redirect
import os
import json
from .models import records
from corescripts.channel import *
from corescripts.pla import *
from corescripts.pca import *
from corescripts.main_pla_pca import *
from corescripts.fkeywords import *
from corescripts.fproductv import *
from corescripts.fk_walllet_balance import *
from corescripts.amazon_scripts.Amazon_campaigns import *
from corescripts.amazon_scripts.amzadgroups import *
from corescripts.amazon_scripts.amz_keywords import *
from corescripts.amazon_scripts.fetching_product_data import *
from corescripts.amazon_scripts.getting_portfolio import *	
import requests
import os



def enter(request):
	return redirect(amazon_Home)




def amazon_Home(request, *args, **kwargs):
	""" Sample Api response that needs to be rendered at frontend. """
	start_date, end_date = '', ''
	request.session["platform"] = "Amazon"
	request.session["wallet_balance"] = "N/A"
	if request.POST:
		print("form submitted")
		inpu_date = request.POST.get('dates', None)
		start_date, end_date = tuple(inpu_date.split('/'))
		print(start_date, end_date)
	
	amzdata = {
			'date': ['2024-02-10', '2024-02-11', '2024-02-12', '2024-02-13', '2024-02-14', '2024-02-15', '2024-02-16', '2024-02-17', '2024-02-18', '2024-02-19', '2024-02-20'],
	        'clicks': ['886', '898', '732', '968', '955', '928', '1007', '972', '904', '728', '860'],
	        'impressions': ['154089', '195622', '167415', '203703', '193190', '196350', '179775', '199966', '169473', '164762', '200250'],
	        'ads_spend': ['12433.1300', '14031.9400', '12181.6100', '15004.5700', '13602.3000', '15325.8600', '15619.3900', '14990.0200', '15057.0200', '12091.8900', '13864.8400'],
	        'total_sales': ['79332.9500', '94769.5600', '63818.6100', '88050.1400', '74313.0300', '93186.6800', '100630.9900', '78241.4900', '85980.7900', '72243.6900', '81547.3400'],
	        'cdcu': ['318', '400', '263', '337', '297', '392', '390', '318', '337', '283', '321'],
	        'roas': ['89.54057562', '105.53403118', '87.18389344', '90.96088843', '77.81469110', '100.41668103', '99.93146971', '80.49536008', '95.11149336', '99.23583791', '94.82248837'],
	        'cvr': ['0.0057', '0.0046', '0.0044', '0.0048', '0.0049', '0.0047', '0.0056', '0.0049', '0.0053', '0.0044', '0.0043'],
	        'cpc': ['14.03287810', '15.62576837', '16.64154372', '15.50058884', '14.24324607', '16.51493534', '15.51081430', '15.42183128', '16.65599558', '16.60973901', '16.12190698'],
	        'aov': ['249.47468553', '236.92390000', '242.65631179', '261.27637982', '250.21222222', '237.72112245', '258.02817949', '246.04242138', '255.13587537', '255.27805654', '254.04155763']
	           
	           }

	platf = request.session['platform']
	bal = request.session['wallet_balance']
	totals = [ sum([int(float(j)) for j in amzdata[i]]) for i in amzdata.keys() if i !='date']
	amzdata['totals'] = totals
	return render(request, "Home_new.html", { 'pf_op':platf, 'balance':bal, 'data':amzdata })





def flipk_Home(request):
	""" Sample Api response that needs to be rendered at frontend. """
	start_date, end_date = str(DT.date.today() - DT.timedelta(days=7)), str(DT.date.today())
	if request.POST:
		print("form submitted")
		inpu_date = request.POST.get('dates', None)
		start_date, end_date = tuple(inpu_date.split('/'))
		print(start_date, end_date)
	
	request.session['platform'] = "Flipkart"
	cookie = cookie_generator()[0]
	request.session["wallet_balance"] = walletbalance(cookie)
	datapca = { # Use this when testing to not get api overload
			'date': ['2024-02-25', '2024-02-26', '2024-02-27', '2024-02-28', '2024-02-29', '2024-03-01', '2024-03-02'],
	        'ads_spend': ['62542.1500', '8701.7000', '6182.6000', '3502.3000', '8544.3000', '943.6000', '14941.6000'],
	        'impressions': ['495896', '89687', '59172', '35209', '94039', '8884', '158555'],
	        'clicks': ['8863', '1252', '904', '460', '1246', '133', '1992'],
	        'ctr': ['0.0179', '0.0140', '0.0153', '0.0131', '0.0132', '0.0150', '0.0126'],
	        'cdcu': ['334', '134', '69', '23', '77', '5', '79'],
	        'cicu': ['32', '2', '13', '0', '0', '0', '12'],
	        'cvr': ['0.0413', '0.1086', '0.0907', '0.0500', '0.0618', '0.0376', '0.0457'],
	        'cdcr': ['156588.0000', '61275.0000', '35229.0000', '9827.0000', '34781.0000', '2069.0000', '33512.0000'],
	        'cicr': ['4362.0000', '238.0000', '1827.0000', '0.0000', '0.0000', '0.0000', '2304.0000'], 
			'roi': ['2.5037', '7.0417', '5.6981', '2.8059', '4.0707', '2.1927', '2.2429']
			}
	
	# datapca = payloadpca(cookie, start_date=start_date, end_date=end_date)
	datapla = payloadpla(cookie, start_date='2024-03-03', end_date='2024-03-09')
 	# print(datapla)


	platf = request.session['platform']
	bal = request.session["wallet_balance"]
	totals = [ sum([int(float(j)) for j in datapla[i]]) for i in datapla.keys() if i !='date']
	datapla['totals'] = totals
	datapla['totals'][3] = float(datapla['totals'][3]/len(datapla['ctr'])) if datapla['totals'][3] !=0 else 0
	datapla['totals'][6] = float(datapla['totals'][6]/len(datapla['cvr'])) if datapla['totals'][6] !=0 else 0
	datapla['totals'][9] = float(datapla['totals'][9]/len(datapla['roi'])) if datapla['totals'][9] !=0 else 0
	print(datapla)

	return render(request, "Home_new.html", { 'pf_op':platf, 'balance':bal, 'data':datapla})




def Portfolio(request):
	start_date, end_date = str(DT.date.today() - DT.timedelta(days=7)), str(DT.date.today())
	platf = request.session['platform']
	bal = request.session["wallet_balance"]

	if platf == 'Amazon':
		if request.POST:
			inpu_date = request.POST.get('dates', None)
			# if inpu_date == None:
			# 	a = request.POST.get('para1', None)
			# 	b = request.POST.get('para2', None)
			# 	c = request.POST.get('para3', None)
			# 	d = request.POST.get('para4', None)
			# 	print(a, b, c, d)

			# sakshi vaval
			# os.system(f"amzpost\enable_disable_campaign.py --p1 {b.lower()}  --p2 {a} --p3 {c}")

			# print("form submitted")
			start_date, end_date = tuple(inpu_date.split('/'))

		amz_portfolio_data = amzPortfolio(start_date= start_date, end_date= end_date)
		
		return render(request, 'amzportfolio.html', {'portfolio': 	amz_portfolio_data, 'balance': bal, 'pf_op':platf, 'data':[]})
	
	
	else:
		return redirect('404')






def Campagins(request):
	start_date, end_date = str(DT.date.today() - DT.timedelta(days=7)), str(DT.date.today())
	platf = request.session['platform']
	if platf == 'Flipkart':
		bal = request.session["wallet_balance"]
		campdata = []
		campdata =[{'campaign_status': 'LIVE', 'campaign_name': 'new giftsets', 'campaign_start_and_end_date': "15 Feb '24 - Till budget ends", 'campaign_type': 'BRAND_PCA', 'campaign_id': 'P0XSUPVCJKA7', 'campaign_budget': '400000.0', 'CTR': '0.0123', 'Cost': '190164.0000', 'total_converted_revenue': '594942.0000', 'clicks': '27188', 'total_converted_units': '1410', 'roi': '3.1286', 'views': '2211218', 'cvr': '0.0519', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","COMMIT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'LIVE', 'campaign_name': 'premium perf', 'campaign_start_and_end_date': "08 Dec '23 - Till budget ends", 'campaign_type': 'BRAND_PLA', 'campaign_id': 'KVACVQ6WVTD6', 'campaign_budget': '1200000.0', 'CTR': '0.0147', 'Cost': '58560.0000', 'total_converted_revenue': '155137.0000', 'clicks': '8860', 'total_converted_units': '275', 'roi': '2.6492', 'views': '601703', 'cvr': '0.0310', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","COMMIT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'LIVE', 'campaign_name': 'Premium Perfumes', 'campaign_start_and_end_date': "04 Dec '23 - Till budget ends", 'campaign_type': 'BRAND_PCA', 'campaign_id': '2EY07O5OXG4Z', 'campaign_budget': '1800000.0', 'CTR': '0.0137', 'Cost': '201891.0500', 'total_converted_revenue': '310496.0000', 'clicks': '24641', 'total_converted_units': '754', 'roi': '1.5379', 'views': '1798400', 'cvr': '0.0306', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","COMMIT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'PAUSED', 'campaign_name': '100ML PERFUME', 'campaign_start_and_end_date': "22 Aug '23 - Till budget ends", 'campaign_type': 'BRAND_PCA', 'campaign_id': 'SI2W9PAB328U', 'campaign_budget': '1700000.0', 'CTR': '0.0111', 'Cost': '3241.7000', 'total_converted_revenue': '6817.0000', 'clicks': '214', 'total_converted_units': '17', 'roi': '2.1029', 'views': '19237', 'cvr': '0.0794', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","USER_RESUME","ABORT","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'BUDGET_MET', 'campaign_name': '100ml Perfumes', 'campaign_start_and_end_date': "02 Aug '23 - Till budget ends", 'campaign_type': 'BRAND_PLA', 'campaign_id': 'FNXDALYUNLQ9', 'campaign_budget': '5490000.0', 'CTR': '0.0134', 'Cost': '462902.8800', 'total_converted_revenue': '2203246.0000', 'clicks': '64284', 'total_converted_units': '4963', 'roi': '4.7596', 'views': '4808299', 'cvr': '0.0772', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'LIVE', 'campaign_name': 'perfume giftset', 'campaign_start_and_end_date': "25 Jul '23 - Till budget ends", 'campaign_type': 'BRAND_PLA', 'campaign_id': 'LVTKB9E6EHUH', 'campaign_budget': '7000000.0', 'CTR': '0.0215', 'Cost': '566985.8500', 'total_converted_revenue': '2041054.0000', 'clicks': '75029', 'total_converted_units': '4365', 'roi': '3.5998', 'views': '3491051', 'cvr': '0.0582', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","COMMIT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'},
				   {'campaign_status': 'TOTAL_BUDGET_MET', 'campaign_name': 'new perfumes', 'campaign_start_and_end_date': "30 Mar '23 - Till budget ends", 'campaign_type': 'BRAND_PLA', 'campaign_id': '7YR8TCCLCKUA', 'campaign_budget': '2800000.0', 'CTR': '0.0102', 'Cost': '128457.7000', 'total_converted_revenue': '275937.0000', 'clicks': '14244', 'total_converted_units': '526', 'roi': '2.1481', 'views': '1397470', 'cvr': '0.0369', 'Actions': '["AUDIT_TRAIL","BCAP_RESUME","COMPLETE","ABORT","ARCARIUS_PAUSE","USER_PAUSE","EDIT","ARCARIUS_RESUME","BCAP_PAUSE"]'}]
		
		if request.POST:
			print("form submitted")
			inpu_date = request.POST.get('dates', None)
			cookie = cookie_generator()[0]
			if inpu_date == None:
				inpu_date = "2024-03-03/2024-03-09"
				# print(campdata)
				a = request.POST.get('para1', None)
				b = request.POST.get('para2', None)
				c = request.POST.get('para3', None)
				d = request.POST.get('para4', None)
				# if c =="":
				# 	print(str(a), str(b))
				# 	os.system(f"universal_pla.py --p1 {a.replace(' ','-')} --p2 {b}")
				# elif a=="":
				# 	os.system(f"universal_pla.py --p2 {b} --p3 {c}")
				# else:
				# 	pass
				# 	os.system(f"pause_resume_hip.py --p1 {a} --p2 {b} --p3 {c} --p4 {d} ")
			start_date, end_date = tuple(inpu_date.split('/'))
			campdata = payloadcampagins(cookie, start_date=start_date, end_date=end_date)
		return render(request, "flipcamp.html", {'campagin':campdata, 'balance': bal, 'pf_op':platf, 'data':[]})
	else:
		bal = request.session["wallet_balance"]
		sd, ed = '2024-02-13', '2024-02-14'
		if request.POST:
			inpu_date = request.POST.get('dates', None)
			if inpu_date == None:
				a = request.POST.get('para1', None)
				b = request.POST.get('para2', None)
				c = request.POST.get('para3', None)
				d = request.POST.get('para4', None)
			print(a, b, c, d)
			os.system(f"amzpost\enable_disable_campaign.py --p1 {b.lower()}  --p2 {a} --p3 {c}")
			# print("form submitted")
			# sd, ed = tuple(inpu_date.split('/'))
		campdata = amzcampagin()
		return render(request, "amzcampagin.html", {'campagin':campdata, 'balance': bal, 'pf_op':platf, 'data':[]})



def Adsgroup(request):
	platf = request.session['platform']
	bal = request.session["wallet_balance"]
	if platf == 'Amazon':
		ads_grp_data = adsGroupData()

		return render(request, "adgroup.html", {'add_group_data':ads_grp_data, 'pf_op':platf, 'data':[], 'balance': bal})
	else:
		return redirect('404')




def keywords(request):
	platf = request.session['platform']
	bal = request.session["wallet_balance"]
	if platf == 'Flipkart':
		keyword = [{'campaign_id': '8VN5DXLKJN8A', 'campaign_name': 'Acne Patch KW PLA', 'adgroup_id': 'YZFM9CTUO7TP', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'BROWSE_PAGE_TOP_SLOT', 'views': 19, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': '8VN5DXLKJN8A', 'campaign_name': 'Acne Patch KW PLA', 'adgroup_id': 'YZFM9CTUO7TP', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'SEARCH_PAGE', 'views': 0, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': '8VN5DXLKJN8A', 'campaign_name': 'Acne Patch KW PLA', 'adgroup_id': 'YZFM9CTUO7TP', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'HOME_PAGE', 'views': 0, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': '8VN5DXLKJN8A', 'campaign_name': 'Acne Patch KW PLA', 'adgroup_id': 'YZFM9CTUO7TP', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'BROWSE_PAGE_TOP_SLOT', 'views': 16, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': '8VN5DXLKJN8A', 'campaign_name': 'Acne Patch KW PLA', 'adgroup_id': 'YZFM9CTUO7TP', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'PRODUCT_PAGE', 'views': 80, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'PRODUCT_PAGE', 'views': 221, 'clicks': 6.0, 'ctr': 2.7149, 'cpc': 2.2, 'cvr': 0, 'adspend': 13.2, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'SEARCH_PAGE_TOP_SLOT', 'views': 0, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'SEARCH_PAGE', 'views': 120, 'clicks': 2.0, 'ctr': 1.6667, 'cpc': 2.2, 'cvr': 0, 'adspend': 4.4, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'BROWSE_PAGE_TOP_SLOT', 'views': 11, 'clicks': 2.0, 'ctr': 18.1818, 'cpc': 2.2, 'cvr': 0, 'adspend': 4.4, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'BROWSE_PAGE_TOP_SLOT', 'views': 33, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}, {'campaign_id': 'OWL1UYKSNRYR', 'campaign_name': 'Hair Removal Spray Generic  KW', 'adgroup_id': 'JJPFWFQ6J2C8', 'adgroup_name': 'Body and Face Skin Care', 'placement_type': 'HOME_PAGE', 'views': 0, 'clicks': 0.0, 'ctr': 0.0, 'cpc': 0.0, 'cvr': 0, 'adspend': 0.0, 'usdir': 0, 'usind': 0, 'revenue': 0, 'Inrevenue': 0, 'roid': 0.0, 'roii': 0.0, 'roas': 0, 'troas': 0, 'service': 'SERVICEABLE', 'category': 'PLA', 'required': 2.2}]
		if request.POST:
			a = request.POST.get('para1', None)
			b = request.POST.get('para2', None)
			c = request.POST.get('para3', None)
			print(a, b, c)
		keyword = flipKeywords()
		return render(request, "flipk_key.html", {'keyword': keyword, 'pf_op':platf, 'balance': bal })
	else:
		keyword = amz_pload()
		return render(request, "amz_key.html", {'keyword': keyword, 'pf_op':platf, 'balance': bal})






def Product(request):
	start_date, end_date = str(DT.date.today() - DT.timedelta(days=7)), str(DT.date.today())
	platf = request.session['platform']
	bal = request.session["wallet_balance"]
	if platf == 'Amazon':
		productdata = []
		
		productdata = package_data(start_date= start_date, end_date= end_date)
		# print(productdata)
		
		return render(request, "amzproduct.html", {'product': productdata, 'balance': bal, 'pf_op':platf, 'data':[]})
	
	else:
		productdata = flipk_payload()
		print(productdata)
		# return None
		return render(request, "fliproduct.html", {'product': productdata, 'balance': bal, 'pf_op':platf, 'data':[]})




def Rule(request, *args, **Kwargs):
	platf = request.session['platform']
	bal = request.session["wallet_balance"]
	return render(request, "later.html", { 'balance': bal, 'pf_op':platf,})






def page_404(request):
	return render(request, 'page_404.html', {})