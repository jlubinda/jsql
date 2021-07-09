import unittest
from jsql import *

class TestJSQL(unittest.TestCase):

	def test_selectall_1A(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT (',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['IN',{"SELECTALL":{"FROM":"table2","WHERE":[
						['INIT',{"col5":['=','value4']}]
						]
						}}]
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry1 = "SELECT * FROM table1 WHERE (col1 = 'value1' AND (col2 LIKE 'value2' OR col3 = 'value3' NOT col4 IN (SELECT * FROM table2 WHERE col5 = 'value4') GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		qry_parqry_params_1ams = ()
		
		js = jsql()
		
		qry_1,params_1,my_key = js.jsonDecoder(jsql_qry1)
		
		assert (qry_1 == sql_qry1)

	def test_selectall_1B(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT (',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['IN',{"SELECTALL":{"FROM":"table2","WHERE":[
						['INIT',{"col5":['=','value4']}]
						]
						}}]
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		jsql_qry2 = {"PROCESS":{
			"DATA":{},
			"USING":"method",
			"FROM":"class",
			"PARAMETERS":{"param1":"value1","param2":"value2","param3":"value3","param4":"value4"}
			}
		}

		jsql_qry3 = {"PROCESS":{
			"DATA":{},
			"USING":"function",
			"PARAMETERS":{"param1":"value1","param2":"value2","param3":"value3","param4":"value4"}
			}
		}

		sql_qry1 = "SELECT * FROM table1 WHERE (col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 IN (SELECT * FROM table2 WHERE col5 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		qry_params_1 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		qry_1,params_1,my_key = js.jsonDecoder(jsql_qry1)
		
		assert (qry_params_1 == params_1)

	def test_selectall_2A(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT ',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['=','value4']
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry2 = "SELECT * FROM table1 WHERE col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		params_2 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		sql_qry1,params,my_key = js.jsonDecoder(jsql_qry1)
		
		assert sql_qry1 == sql_qry2



	def test_selectall_2B(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT ',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['=','value4']
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry2 = "SELECT * FROM table1 WHERE col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		params_2 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		sql_qry1,params,my_key = js.jsonDecoder(jsql_qry1)
		
		assert params == params_2


	##################################
	def test_select_1A(self):
		jsql_qry1 = {"SELECT":{"COLS":['col1','col2','col3'],
			"FROM":"table1",
			"WHERE":[
					['INIT (',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['IN',{"SELECTALL":{"FROM":"table2","WHERE":[
						['INIT',{"col5":['=','value4']}]
						]
						}}]
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry1 = "SELECT col1,col2,col3 FROM table1 WHERE (col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 IN (SELECT * FROM table2 WHERE col5 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		js = jsql()
		
		qry_1,params_1,my_key = js.jsonDecoder(jsql_qry1)
		
		assert (qry_1 == sql_qry1)

	def test_select_1B(self):
		jsql_qry1 = {"SELECT":{"COLS":['col1','col2','col3'],
			"FROM":"table1",
			"WHERE":[
					['INIT (',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['IN',{"SELECTALL":{"FROM":"table2","WHERE":[
						['INIT',{"col5":['=','value4']}]
						]
						}}]
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry1 = "SELECT col1,col2,col3 FROM table1 WHERE (col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 IN (SELECT * FROM table2 WHERE col5 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		qry_params_1 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		qry_1,params_1,my_key = js.jsonDecoder(jsql_qry1)
		
		assert (qry_params_1 == params_1)

	def test_select_2A(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT ',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['=','value4']
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry2 = "SELECT * FROM table1 WHERE col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		params_2 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		sql_qry1,params,my_key = js.jsonDecoder(jsql_qry1)
		
		assert sql_qry1 == sql_qry2



	def test_select_2B(self):
		jsql_qry1 = {"SELECTALL":{
			"FROM":"table1",
			"WHERE":[
					['INIT ',{
						"col1":['=','value1']
					}],
					['AND (',{
						"col2":['LIKE','value2']
					}],
					['OR',{
						"col3":['=','value3']
					}],
					['NOT',{
						"col4":['=','value4']
					}],
					[') END']
				],
			"GROUPBY":["col6","col7","col8"],
			"ORDERBY":[
					["col9","col10","col11"],"DESC"
				]
			}
		}

		sql_qry2 = "SELECT * FROM table1 WHERE col1 = $1 AND (col2 LIKE $2 OR col3 = $3 NOT col4 = $4) GROUPBY col6,col7,col8 ORDERBY col9,col10,col11 DESC"
		
		params_2 = ['value1','value2','value3','value4']
		
		js = jsql()
		
		sql_qry1,params,my_key = js.jsonDecoder(jsql_qry1)
		
		assert params == params_2

	def test_process_1A(self):

		jsql_qry2 = {"PROCESS":{
			"DATA":{"param1":"value1","param2":"value2","param3":"value3","param4":"value4"},
			"USING":"method",
			"FROM":"module.submodule.myclass",
			"WITH":""
			}
		}
