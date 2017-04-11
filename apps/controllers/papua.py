import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'papua'
		provloc = '135.220428, -5.231223'
		mapzoom = '7'
		kabkotcord = [
		'140.480464, -8.503258',
		'139.415294, -4.347261',
		'140.644632, -2.591545',
		'135.515479, -3.463997',
		'136.104039, -1.702560',
		'135.929511, -0.878215',
		'136.301946, -3.623314',
		'137.159496, -4.078749',
		'136.544838, -4.464788',
		'140.211462, -5.436491',
		'139.101504, -6.355493',
		'138.525013, -5.318847',
		'139.350852, -4.175618',
		'140.475505, -4.149516',
		'138.397951, -3.388663',
		'140.7624493, -3.3449536',
		'136.670534, -2.8435717',
		'135.6385125, -0.7295099',

		'137.7637565, -2.5331255',
		'138.2393528, -4.4069496',
		'138.3190276, -3.971033',
		'138.3190276, -2.3745692',
		'139.4466005, -3.7852847',
		'137.6061625, -3.8649098',
		'135.6763443, -4.0454139',
		'136.569279, -3.392247',
		'136.4393054,-4.0974893',
		'140.6689995, -2.5916025'

		]
		listkabkot = [
		'%9401%','%9402%','%9403%','%9404%','%9408%','%9409%','%9410%',
		'%9411%','%9412%','%9413%','%9414%','%9415%','%9416%','%9417%','%9418%','%9419%','%9420%',
		'%9426%','%9427%','%9428%','%9429%','%9430%',
		'%9431%','%9432%','%9434%','%9435%','%9436%'
		'%9471%'
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