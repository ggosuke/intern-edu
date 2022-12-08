from flask import Blueprint, jsonify, request
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
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
  day_of_week: str
  datetime: str
  name: str
  classroom: str
  links: Iterable[str]
  teacher: str
  id: str
  weeklytasks: Iterable[ClassTask]
  generaltask: Iterable[ClassTask]



class_date = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d %H%M')
class_rough_datas = {
  "00001" : ClassData(day_of_week="Monday", datetime=class_date, name="線形代数", id='0001'),
}
class_detail_datas = {
  "00001": ClassDetailsData(
            day_of_week="Monday", datetime=class_date, name="線形代数", id="00001",
            classroom="F123", 
            links=["https://ibm.webex.com/ibm-jp/j.php?MTID=m0372978239d101675d877a7c6ded9a5b"],
            teacher="aaa",
            weeklytasks=[], generaltask=[])
}


# Blueprint
app = Blueprint('hello', __name__)

api_base = Path("/api")

@app.route(str(api_base / 'getCalender'), methods=["GET"])
def getcalend():
  data: Dict[str, Any] = {"status": 200}
  data['carenders'] = list(class_detail_datas.values())

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

@app.route(str(api_base / "putCarender/<class_id>"), methods=["PUT"])
def putcarend(class_id):
  message = {}
  data = {}
  if class_id not in class_detail_datas:
    return jsonify(data), 204

  class_data = class_detail_datas[class_id]
  body = request.json
  for key in body.keys():
    setattr(class_data, key, body[key])

  message['classdata'] = class_data
  data['status'] = 200
  data['data'] = message
  return jsonify(data), 200

@app.route(str(api_base / "getTasks"))
def gettasks():
  ...

