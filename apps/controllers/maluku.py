import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'maluku'
		provloc = '130.106357, -3.230494'
		mapzoom = '9'
		kabkotcord = [
		'131.434049, -7.567118',
		'132.732840, -5.773130',
		'129.367758, -3.105895',
		'126.782889, -3.382086',
		'134.543380, -6.185020',
		'128.363830, -3.081290',
		'130.412647, -3.396104',
		'126.285373, -7.788836',
		'126.256799, -3.467444',
		'128.105698, -3.621720',#71
		'132.300265, -5.626926'
		]
		listkabkot = [
		'%8101%','%8102%','%8103%','%8104%','%8105%','%8106%','%8107%','%8108%','%8109%',
		'%8171%','%8172%'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		return dt