#login with default docID(?)
#purchaselist(surgey) only one instrument and equipment being allowed, adding problem and comment column to update to DB, adding delete buttom
#purchaser adding new item which means the html should be dymatic using the parameters. Need to add fuction to get all category
#appiontment showing, searching, update with docID, appointment will influence dia and ope(inv_ID) also proble and comment  
from flask import Flask, request, jsonify, render_template, redirect, url_for, render_template_string,session
from dbms_function import DBMSFunction
import pymysql
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key
dbms = DBMSFunction()

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/test_db")
def test_db():
    try:
        conn = pymysql.connect(**dbms.db_settings)
        return "資料庫連線成功"
    except Exception as ex:
        return f"資料庫連線失敗: {ex}"
    finally:
        if conn:
            conn.close()


@app.route("/login-doctor", methods=['GET', 'POST'])
def login_doctor():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if dbms.登入登出d(name, password):
            doctor_id = dbms.get_doctor_id(name)  # 获取医生ID
            if doctor_id:
                session['username'] = name
                session['role'] = 'doctor'
                session['doctor_id'] = doctor_id  # 保存医生ID到session
                return redirect(url_for('doctor'))
            else:
                error = "Doctor ID not found"
                return render_template('login-doctor.html', error=error)
        else:
            error = "Invalid username or password"
            return render_template('login-doctor.html', error=error)
    return render_template('login-doctor.html')



@app.route("/login-purchaser", methods=['GET', 'POST'])
def login_purchaser():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if dbms.登入登出p(name, password):
            session['username'] = name
            session['role'] = 'purchaser'
            return redirect(url_for('purchaser'))
        else:
            error = "Invalid username or password"
            return render_template('login-purchaser.html', error=error)
    return render_template('login-purchaser.html')

@app.route("/login-administrator", methods=['GET', 'POST'])
def login_administrator():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if dbms.登入登出a(name, password):
            session['username'] = name
            session['role'] = 'administrator'
            return redirect(url_for('admin_first'))
        else:
            error = "Invalid username or password"
            return render_template('login-administrator.html', error=error)
    return render_template('login-administrator.html')

@app.route("/doctor")
def doctor():
    if 'role' in session and session['role'] == 'doctor':
        return render_template('doctor.html')
    else:
        return redirect(url_for('main'))


@app.route('/patientdata', methods=['GET', 'POST'])
def patientdata():
    doctor_id = session.get('doctor_id')
    patients = []
    if doctor_id:
        patients = dbms.get_patients_by_doctor_id(doctor_id)  # 获取医生的病人列表

    if request.method == 'POST':
        patient_id = request.form.get('id')
        action = request.form.get('action')
        if action == 'search':
            # 显示病人的历史资料
            result = dbms.更新資料('patient', patient_id, 'query', column='*')
            if result:
                return render_template('doctor_patient.html', patient=result, patients=patients)
            else:
                # return render_template_string("No patient data found")
                return render_template_string("<script>alert('No patient data found'); window.location.href = '/patientdata';</script>")
    return render_template('doctor_patient.html', patients=patients)

@app.route('/surgery', methods=['GET', 'POST'])
def surgery():
    if request.method == 'POST':
        instruments = request.form.getlist('instrument[]')
        equipment_values = request.form.getlist('equipment[]')
        additional_equipment = request.form.get('additional_equipment')
        additional_quantity = request.form.get('additional_quantity')
        problem = request.form.get('problem')
        comment = request.form.get('comment')

        equipment_names = [
            '手術刀', 'PVC手套', '果凍凝膠面罩', '生理食鹽水', 
            '紗布', '面膜紙', '麻醉藥劑', '肉毒桿菌素', 
            '酒精棉片', '玻尿酸'
        ]

        # 获取最新的 Inventory_ID 和 Consumables 名称对
        result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')
        
        # 将结果转换为字典
        equipment_dict = {name: inv_id for inv_id, name in result}
        
        try:
            # 處理 equipment 值
            for name, value in zip(equipment_names, equipment_values):
                if name in equipment_dict and value:
                    insert_value = int(value)
                    if insert_value != 0:
                        insert_data = {
                            'Tool': instruments,
                            'Inventory_ID': equipment_dict[name],
                            'Amount': insert_value,
                            'Problem': problem,
                            'Comment': comment
                        }
                        dbms.插入資料('operation', insert_data)
                        # 更新inventory表內物品數量，減少使用的數量
                        dbms.更新資料('inventory', equipment_dict[name], 'addup', column='Amount', new_item=-insert_value)
            
            # 處理下拉選單選擇的 additional equipment 值
            if additional_equipment in equipment_dict and additional_quantity:
                insert_value = int(additional_quantity)
                if insert_value != 0:
                    insert_data = {
                        'Tool': instruments,
                        'Inventory_ID': equipment_dict[additional_equipment],
                        'Amount': insert_value
                    }
                    #dbms.插入資料('operation', insert_data)
                    # 更新inventory表內物品數量，減少使用的數量
                    dbms.更新資料('inventory', equipment_dict[additional_equipment], 'addup', column='Amount', new_item=-insert_value)

            return render_template_string("<script>alert('Data updated'); window.location.href = '/surgery';</script>")
        except Exception as e:
            print(f"Database error: {e}")
            return render_template_string("<script>alert('Error updating data'); window.location.href = '/surgery';</script>")
    return render_template('doctor_surgery.html')

@app.route('/diagnose', methods=['GET', 'POST'])
def diagnose():
    if request.method == 'POST':
        equipment = request.form.get('equipment')
        quantity = request.form.get('quantity')
        problem = request.form.get('problem')
        comment = request.form.get('comment')

        # 获取最新的 Inventory_ID 和 Consumables 名称对
        result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')

        # 将结果转换为字典
        equipment_dict = {name: inv_id for inv_id, name in result}

        try:
            if equipment in equipment_dict and quantity:
                insert_data = {
                    'Inventory_ID': equipment_dict[equipment],
                    'Amount': int(quantity),
                    'Problem': problem,
                    'Comment': comment
                }
                dbms.插入資料('diagnose', insert_data)
                
                # Update the equipment inventory
                success, message = update_equipment_inventory(equipment, quantity)
                if not success:
                    return render_template_string(f"<script>alert('{message}'); window.location.href = '/diagnose';</script>")

            return render_template_string("<script>alert('Data updated'); window.location.href = '/diagnose';</script>")
        except Exception as e:
            print(f"Database error: {e}")
            return render_template_string(f"<script>alert('Error updating data: {e}'); window.location.href = '/diagnose';</script>")

    try:
        items = dbms.get_items_from_inventory()
    except Exception as e:
        print(f"Database error: {e}")
        items = []

    result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')
    equipment_names = [name for _, name in result]

    return render_template('doctor_diagnose.html', items=items, equipment_names=equipment_names)

def update_equipment_inventory(equipment, quantity):
    try:
        result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')
        equipment_dict = {name: inv_id for inv_id, name in result}
        
        if equipment in equipment_dict and quantity:
            dbms.更新資料('inventory', equipment_dict[equipment], 'addup', 'Amount', -int(quantity))
            return True, "Data updated"
    except Exception as e:
        print(f"Database error: {e}")
        return False, "Error updating data"

@app.route('/purchaser', methods=['GET', 'POST'])
def purchaser():
    if 'role' not in session or session['role'] != 'purchaser':
        return redirect(url_for('main'))

    if request.method == "GET":
        result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')
        equipment_names = [name for _, name in result]
        items = dbms.get_items_from_inventory()
        return render_template('purchaser.html', items=items, equipment_names=equipment_names)
    
    if request.method == 'POST':
        equipment = request.form.get('equipment')
        quantity = request.form.get('quantity')

        # 獲取最新的 Inventory_ID 和 Consumables 名稱對
        result = dbms.顯示資料("Inventory_ID,Consumables", sheet='inventory')
        
        # 將結果轉換為字典
        equipment_dict = {name: inv_id for inv_id, name in result}
        
        try:
            if equipment in equipment_dict and quantity:
                dbms.更新資料('inventory', equipment_dict[equipment], 'addup', 'Amount', int(quantity))
                return render_template_string("<script>alert('Data updated'); window.location.href = '/purchaser';</script>")
        except Exception as e:
            print(f"Database error: {e}")
            # return render_template_string("Error updating data")
            return render_template_string("<script>alert('Error updating data'); window.location.href = '/purchaser';</script>")
    
    # 獲取更新後的數據
    try:
        items = dbms.get_items_from_inventory()
    except Exception as e:
        print(f"Database error: {e}")
        items = []

    # 將設備名稱列表傳遞給模板
    equipment_names = [name for _, name in result]
    return render_template('purchaser.html', items=items, equipment_names=equipment_names)

@app.route('/api/items', methods=['GET'])
def get_items():
    result = dbms.get_items_from_inventory()
    return jsonify(result)

@app.route("/admin_first")
def admin_first():
    if 'role' in session and session['role'] == 'administrator':
        return render_template('administrator_first.html')
    else:
        return redirect(url_for('main'))

@app.route('/administrator', methods=['GET', 'POST'])  #更新預約紀錄
def administrator():
    if 'role' not in session or session['role'] != 'administrator':
        return redirect(url_for('main'))
    
    appointments = []
    if request.method == "GET":
        appointments=[]
    if request.method == 'POST':
        try:
            patient_id = request.form.get('patientid')
            doctor_id = request.form.get('doctorid')
            date = request.form.get('date')
            action = request.form.get('action') #diagnose or operation
            final_action = request.form.get('action2') #update or search
            print(f"Received action: {final_action}")  # 调试输出 action
            # 解析原始日期字符串
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
            # 格式化为目标日期字符串
            formatted_date = date_obj.strftime('%Y/%m/%d %H:%M')
            if final_action == 'update':
                dbms.掛號資料插入(patient_id,doctor_id,action,formatted_date)
                # return render_template_string("Data submitted")
                return render_template_string("<script>alert('Patient data updated'); window.location.href = '/administrator';</script>")
                
            # elif final_action == 'search':
            #     result = dbms.更新資料('appointment', doctor_id, 'query', column='*')
            #     if result:
            #         return render_template('administrator.html', appointment=result)
            #     else:
            #         return render_template_string("No patient data found")
        except Exception as e:
            print(f"Database error: {e}")
            appointments = []
    return render_template('administrator.html', appointments=appointments)

@app.route('/adminpatient', methods=['GET', 'POST'])
def adminpatient():
    if request.method == 'POST':
        patient_id = request.form.get('id')
        datetime = request.form.get('date')
        name = request.form.get('name')
        Fname = name.split(" ")[0] if name else ''
        LName = name.split(" ")[1] if len(name.split(" ")) > 1 else ''
        Phonenumber = request.form.get('phone')
        Authorize = request.form.get('authorize')
        action = request.form.get('action')
        try:
            if action == 'search':
                result = dbms.更新資料('patient', patient_id, 'query', column='*')
                if result:
                    return render_template('administrator_patient.html', patient=result)
                else:
                    return render_template_string("<script>alert('No patient data found'); window.location.href = '/adminpatient';</script>")
            elif action == 'update':
                if Fname: dbms.更新資料('patient', patient_id, 'update', column='Fname', new_item=Fname)
                if LName: dbms.更新資料('patient', patient_id, 'update', column='LName', new_item=LName)
                if datetime: dbms.更新資料('patient', patient_id, 'update', column='Birth_Date', new_item=datetime)
                if Phonenumber: dbms.更新資料('patient', patient_id, 'update', column='Phone_number', new_item=Phonenumber)
                if Authorize: dbms.更新資料('patient', patient_id, 'update', column='Authorize', new_item=Authorize)              
                return render_template_string("<script>alert('Patient data updated'); window.location.href = '/adminpatient';</script>")
            elif action == 'insert':
                numberid = patient_id.split("t")[1]
                try:
                    dbms.更新資料('patient', patient_id, 'insert into', column='patient_id,number,Fname,LName,Birth_Date,Phone_number,Authorize', new_item=(patient_id,numberid,Fname,LName,datetime,Phonenumber,Authorize))
                    return render_template_string("<script>alert('Patient data inserted'); window.location.href = '/adminpatient';</script>")
                except Exception as e:
                    return render_template_string(f"<script>alert('Insert failed: {str(e)}'); window.location.href = '/adminpatient';</script>")
            elif action == 'delete':
                dbms.更新資料('patient', patient_id, 'delete')
                return render_template_string("<script>alert('Patient data deleted'); window.location.href = '/adminpatient';</script>")
        except Exception as e:
            return render_template_string(f"Database error: {e}")
    return render_template('administrator_patient.html')


if __name__ == '__main__':
    app.run(debug=True)

#pages return button or new window
