import pymysql
from datetime import datetime

class DBMSFunction:
    def __init__(self):
        self.db_settings = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "Kevin306051",
            "db": "hospital",
            "charset": "utf8"
        }
        self.user_passd = {
            "Doc1": "doc_pass",
            "Doc2": "doc_pass",
            "Doc3": "doc_pass",
            "Doc4": "doc_pass",
            "Doc5": "doc_pass",
        }
        self.user_passp = {
            "pur": "pur_pass",
        }
        self.user_passa = {
            "adm": "adm_pass"
        }
                
        # 獲取當前日期和時間
        current_date = datetime.now()

        # 格式化日期為字符串
        formatted_date = current_date.strftime("%Y/%m/%d %H:%M")
        print("今天的日期是：", formatted_date)

    def 登入登出d(self, user_name, user_password):
        return self.user_passd.get(user_name) == user_password
    def 登入登出p(self, user_name, user_password):
        return self.user_passp.get(user_name) == user_password
    def 登入登出a(self, user_name, user_password):
        return self.user_passa.get(user_name) == user_password

    def 更新資料(self, sheet, primary_id, operation, column='Amount', new_item=''):
        id_column_name = 'Employee_ID' if sheet in ['administration staff', 'doctor', 'buyer'] else f'{sheet.capitalize()}_ID'
        conn = None  # Initialize conn to None
        try:
            conn = pymysql.connect(**self.db_settings)
            with conn.cursor() as cursor:
                if operation == 'update':
                    update_sql = f"UPDATE `{sheet}` SET `{column}` = %s WHERE {id_column_name} = %s"
                    print(update_sql)
                    cursor.execute(update_sql, (new_item, primary_id))

                elif operation == 'insert into':
                    # Check if ID already exists
                    check_sql = f"SELECT COUNT(*) FROM `{sheet}` WHERE {id_column_name} = %s"
                    cursor.execute(check_sql, (primary_id,))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        raise Exception(f"ID {primary_id} already exists in {sheet}")
                    
                    # Convert column to list
                    columns = column.split(',')
                    # Generate placeholders based on the number of columns
                    placeholders = ', '.join(['%s'] * len(columns))
                    # Construct the SQL statement
                    insert_sql = f"INSERT INTO {sheet} ({column}) VALUES ({placeholders})"
                    print(insert_sql)                    
                    # Convert new_item to tuple to match execute method's requirements
                    if not isinstance(new_item, tuple):
                        new_item = tuple(new_item)                    
                    cursor.execute(insert_sql, new_item)
                    print(f"Inserted {column} as {new_item} for ID {primary_id}")

                elif operation == 'delete':
                    if sheet == 'inventory':
                        select_sql_1 = f"SELECT Operation_ID FROM operation WHERE {id_column_name} = %s"
                        select_sql_2 = f"SELECT Purchaselist_ID FROM purchaselist WHERE {id_column_name} = %s"
                        cursor.execute(select_sql_1, (primary_id,))
                        myres_1 = cursor.fetchall()
                        for x in myres_1:
                            self.更新資料('operation', x[0], 'delete')
                        cursor.execute(select_sql_2, (primary_id,))
                        myres_2 = cursor.fetchall()
                        for x in myres_2:
                            self.更新資料('purchaselist', x[0], 'delete')
                        delete_sql = f"DELETE FROM `{sheet}` WHERE {id_column_name} = %s"
                        cursor.execute(delete_sql, (primary_id,))
                    elif sheet in ["doctor", "patient", "buyer"]:
                        select_sql = f"SELECT appointment_ID FROM appointment WHERE {id_column_name} = %s" if sheet != "buyer" else f"SELECT Purchaselist_ID FROM purchaselist WHERE {id_column_name} = %s"
                        cursor.execute(select_sql, (primary_id,))
                        myres = cursor.fetchall()
                        for x in myres:
                            self.更新資料('appointment' if sheet != 'buyer' else 'purchaselist', x[0], 'delete')
                        delete_sql = f"DELETE FROM `{sheet}` WHERE {id_column_name} = %s"
                        cursor.execute(delete_sql, (primary_id,))
                    else:
                        delete_sql = f"DELETE FROM `{sheet}` WHERE {id_column_name} = %s"
                        cursor.execute(delete_sql, (primary_id,))
                    print(f"Deleted record with ID {primary_id}")

                elif operation == 'addup':
                    addup_sql = f"UPDATE `{sheet}` SET {column} = {column} + %s WHERE {id_column_name} = %s"
                    print(addup_sql)
                    cursor.execute(addup_sql, (new_item, primary_id))
                    print(f"Added {new_item} to existing {column} for ID {primary_id}")

                elif operation == 'query':
                    query_sql = f"SELECT {column} FROM `{sheet}` WHERE {id_column_name} = %s"
                    print(query_sql)
                    cursor.execute(query_sql, (primary_id,))
                    result = cursor.fetchone()
                    if result:
                        return result
                conn.commit()
        except Exception as ex:
            print(f"Error: {ex}")
            if conn:
                conn.rollback()
            raise  # Re-raise the exception so it can be caught in the route
        finally:
            if conn:
                conn.close()


    def 顯示資料(self,column,sheet):
    # Capitalize the sheet name and prepare the ID column name
        try:
            # Connect to the database
            conn = pymysql.connect(**self.db_settings)
            #print("连接成功！")

            with conn.cursor() as cursor:
                # Prepare the SQL query statement

                query_sql = f"SELECT {column} FROM `{sheet}` "
                print(query_sql)
                cursor.execute(query_sql)
                result = cursor.fetchall()
                result_list=[]
                if result:
                    for row in result:
                        #print(row)
                        result_list.append(row)
                    #print(result_list)
                    return result_list
                else:
                    print(f"No record found")
                # Commit the transaction
                conn.commit()
                #print("操作成功")

        except Exception as ex:
            print(f"发生错误：{ex}")
            if conn:
                conn.rollback()  # Roll back in case of an error

        finally:
            # Ensure the connection is always closed
            if conn:
                conn.close()

    def 插入資料(self, sheet, data_dict):
        if sheet in ['administration staff', 'doctor', 'buyer']:
            id_column_name = 'Employee_ID'
        else:
            id_column_name = f'{sheet.capitalize()}_ID'
        try:
            conn = pymysql.connect(**self.db_settings)
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT MAX(`Number`) FROM `{sheet}`")
                fetch_result = cursor.fetchone()
                max_id = fetch_result[0] if fetch_result[0] is not None else 0
                next_id = max_id + 1
                data_dict[id_column_name] = f'{sheet[0:3].capitalize()}{next_id}'
                data_dict['Number'] = next_id
                columns = ', '.join(f"`{column}`" for column in data_dict.keys())
                placeholders = ', '.join(['%s'] * len(data_dict))
                insert_sql = f"INSERT INTO `{sheet}` ({columns}) VALUES ({placeholders})"
                print(insert_sql)
                print(tuple(data_dict.values()))
                cursor.execute(insert_sql, tuple(data_dict.values()))
                conn.commit()
        except Exception as ex:
            print(f"Error: {ex}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()

    def get_items_from_inventory(self):
        try:
            conn = pymysql.connect(**self.db_settings)
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                query_sql = """
                    SELECT 
                        Consumables as name, 
                        Amount as quantity, 
                        Unit_Price as unit_price, 
                        (Amount * Unit_Price) as total_price 
                    FROM inventory
                """
                cursor.execute(query_sql)
                result = cursor.fetchall()
                return result
        except Exception as ex:
            print(f"Database error: {ex}")
            return {"error": str(ex)}
        finally:
            if conn:
                conn.close()

    def get_patients_by_doctor_id(self, doctor_id):
        try:
            conn = pymysql.connect(**self.db_settings)
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                query_sql = """
                    SELECT p.Patient_ID
                    FROM appointment a
                    JOIN patient p ON a.Patient_ID = p.Patient_ID
                    WHERE a.Employee_ID = %s
                """
                cursor.execute(query_sql, (doctor_id,))
                result = cursor.fetchall()
                return result
        except Exception as ex:
            print(f"Database error: {ex}")
            return []
        finally:
            if conn:
                conn.close()
    
    def get_doctor_id(self, doctor_name):
        try:
            conn = pymysql.connect(**self.db_settings)
            with conn.cursor() as cursor:
                query_sql = "SELECT Employee_ID FROM doctor WHERE Employee_ID = %s"
                cursor.execute(query_sql, (doctor_name,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except Exception as ex:
            print(f"Database error: {ex}")
            return None
        finally:
            if conn:
                conn.close()

    def 購買材料(self,Inv_id,Purchaser,Unit_Price,Purchase_amount):
        data_to_insert = {
        'Employee_ID' :  Purchaser,
        'Inventory_ID':  Inv_id,
        'Unit_Price'  :  Unit_Price,
        'Amount'      :  Purchase_amount,
        'Total_Price' :  Unit_Price*Purchase_amount
        }
        self.插入資料('purchaselist', data_to_insert)
        Old_amount=self.更新資料('inventory',Inv_id,'query','Amount')
        self.更新資料('inventory',Inv_id,'addup','Amount',Purchase_amount)
        New_amount=self.更新資料('inventory',Inv_id,'query','Amount')
        print('原始數量: {} ,購買後數量: {}'.format(Old_amount,New_amount))

    def 掛號資料插入(self,Patient_ID,Doctor_ID,Fuction,Time):
        if Time==None:
            Time==self.formatted_date
        #function= diagnose or operation
        try:
            print('start')
            # Connect to the database
            conn = pymysql.connect(**self.db_settings)
            print("连接成功！")
            with conn.cursor() as cursor:
                    # Retrieve the last Inventory_ID and increment it
                    cursor.execute(f"SELECT MAX(`Number`) FROM `{Fuction}`")
                    fetch_result = cursor.fetchone()  # Fetch the result
                    max_id = fetch_result[0]
                    if max_id is not None:
                        next_id = max_id + 1
                    else:
                        next_id = 1  # Start from 1 if no IDs are present yet
                    data= Fuction[0:3].capitalize()+str(next_id)

                    data_to_insert = {
                        'Patient_ID': Patient_ID,
                        'Employee_ID':Doctor_ID,
                        'Dia_Ope':data,
                        'Time':Time
                    }
                    print(data_to_insert)
                    self.插入資料('appointment', data_to_insert)

                    data_to_insert = {
                        'Inventory_ID':'TBD',
                        'Amount':0,
                    }
                    self.插入資料(Fuction, data_to_insert)

        except Exception as ex:
            print(f"发生错误：{ex}")
            if conn:
                conn.rollback()  # Roll back in case of an error

        finally:
            # Ensure the connection is always closed
            if conn:
                conn.close()

    def 刪除掛號資料(self,App_ID):
        try:
            # Connect to the database
            conn = pymysql.connect(**self.db_settings)
            print("连接成功！")
            Dia_Ope=self.更新資料('appointment',App_ID,'query','Dia_Ope')

            with conn.cursor() as cursor:
                # 刪除掛號資料
                cursor.execute(f"DELETE FROM `appointment` WHERE `Appointment_ID` = '{App_ID}'")
                # 根據掛號資料ID刪除相關的 dia 和 ope 資料
                if Dia_Ope[:3]=='Dia':
                    Function ='diagnose'

                elif Dia_Ope[:3]=='Ope':
                    Function ='operation'

                Function_capitalized = Function.capitalize()
                id_Function = f'{Function_capitalized}_ID'
                print('id_Function: {} ,PrimaryKey: {} '.format(id_Function,Dia_Ope))
                cursor.execute(f"DELETE FROM `{Function}` WHERE `{id_Function}` = '{Dia_Ope}'")

                # 如果成功刪除資料，提交事務
                conn.commit()

        except Exception as ex:
            print(f"发生错误：{ex}")
            if conn:
                conn.rollback()  # Roll back in case of an error

        finally:
            # Ensure the connection is always closed
            if conn:
                conn.close()
