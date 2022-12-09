from flask import Blueprint, jsonify, request
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, timedelta
import pytz
from typing import Iterable, Dict, Any

@dataclass
class ClassData:
  day_of_week: str
  datetime: str
  name: str
  id: str

@dataclass
class ClassTask:
    limitdate: str
    link: str
    title: str

@dataclass
class ClassDetailsData:
  starttime: str
  endtime: str
  name: str
  classroom: str
  links: Iterable[str]
  teacher: str
  id: str
  tasks: Iterable[ClassTask]



class_startdate = datetime.now(pytz.timezone('Asia/Tokyo'))
class_enddata = class_startdate + timedelta(minutes=90)
class_startdate_str = class_startdate.strftime('%Y-%m-%dT%H:%M:00')
class_enddata_str = class_enddata.strftime('%Y-%m-%dT%H:%M:00')

class_names = [f"授業{i}" for i in range(0, 10)]

class_rough_datas = {
  "00001" : ClassData(day_of_week="Monday", datetime=class_startdate_str, name="線形代数", id='0001'),
}
# class_detail_datas = {
#   "00001": ClassDetailsData(
#             day_of_week="Monday", starttime=class_startdate_str, endtime=class_enddata_str, name="線形代数", id="00001",
#             classroom="F123", 
#             links=["https://ibm.webex.com/ibm-jp/j.php?MTID=m0372978239d101675d877a7c6ded9a5b"],
#             teacher="aaa",
#             weeklytasks=[], generaltask=[])
# }

class_detail_datas = {}
now = datetime.now(pytz.timezone('Asia/Tokyo')) 
today_h_m_d = [now.year, now.month, 1]
for i in range(0, 30):
    for j in range(0, 5):
        class_startdate = datetime(*today_h_m_d, hour=9) + timedelta(days=i) + timedelta(minutes=95 * j)
        class_enddata = class_startdate + timedelta(minutes=90)
        class_startdate_str = class_startdate.strftime('%Y-%m-%dT%H:%M:00')
        class_enddata_str = class_enddata.strftime('%Y-%m-%dT%H:%M:00')
        weekday = class_startdate.weekday()
        if weekday in (5,6): continue
        class_id = f"{weekday:02}{j:02}-{i:02}{j:02}"
        class_detail_datas[class_id] =  ClassDetailsData(
                    starttime=class_startdate_str, endtime=class_enddata_str, name=f"授業 {weekday}-{j}", id=class_id,
                    classroom="F123", 
                    links=["http://google.com", "https://google.co.jp"],
                    teacher="教員", tasks=[])

# Blueprint
app = Blueprint('hello', __name__)

api_base = Path("/api")

user_classname_data = {
  
}

@app.route(str(api_base / 'getCalender'), methods=["GET"])
def getcalend():
  data: Dict[str, Any] = {"status": 200}
  data['calendar'] = list(class_detail_datas.values())

  return jsonify(data), 200


@app.route(str(api_base / "getCalenderDetail/<class_id>"), methods=["GET"])
def getCalenderDetail(class_id):
  data: Dict[str, Any] = {"status": 204}
  status = 204
  class_detail = class_detail_datas.get(class_id)
  if class_detail is not None:
    data['classdata'] = class_detail
    data["status"] = 200
    status = 200

  return jsonify(data), status

@app.route(str(api_base / "putCalenderDetail/<class_id>"), methods=["PUT"])
def putcarend(class_id):
  message = {}
  data = {}
  if class_id not in class_detail_datas:
    return jsonify(data), 204

  class_data = class_detail_datas[class_id]
  body = request.json
  for key in body.keys():
    value = body[key]
    if isinstance(value, list):
      value = [i for i in value if i is not None]
    setattr(class_data, key, value)

  message['classdata'] = class_data
  data['status'] = 200
  data['data'] = message
  return jsonify(data), 200

@app.route(str(api_base / "newCalenderDetail"), methods=["POST"])
def newcarend():
  message = {}
  data = {}
  body = request.json
  new_class = ClassDetailsData(**body)
  class_detail_datas[new_class.id] = new_class
  message['classdata'] = new_class
  data['status'] = 200
  data['data'] = message
  return jsonify(data), 200

@app.route(str(api_base / "deleteCalenderDetail/<class_id>"), methods=["DELETE"])
def delcarend(class_id):
  message = {}
  data = {}
  del_class = class_detail_datas.pop(class_id) 
  message['classdata'] = del_class
  data['status'] = 200
  data['data'] = message
  return jsonify(data), 200

@app.route(str(api_base / "getTasks"))
def gettasks():
  ...

