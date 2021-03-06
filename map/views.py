from django.shortcuts import render
import  folium
from pyrebase import pyrebase
from folium.features import DivIcon
firebaseConfig = {
  "apiKey": "AIzaSyDVni-LWmlVqUE5ZeRhb3iqLSbn4Gjb0RY",
  "authDomain": "dkcongthoatnuoc.firebaseapp.com",
  "databaseURL": "https://dkcongthoatnuoc-default-rtdb.firebaseio.com",
  "projectId": "dkcongthoatnuoc",
  "storageBucket": "dkcongthoatnuoc.appspot.com",
  "messagingSenderId": "769607464501",
  "appId": "1:769607464501:web:cef8828c5f3236c624e37c",
  "measurementId": "G-D2LKM5HM2K"
}
firebase=pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
db=firebase.database()

# Create your views here.

def index(request):
    #Creat map object
    benngoai1 = db.child("NODE1").child("ben ngoai").get().val()
    bentrong1 = db.child("NODE1").child("ben trong").get().val()
    id1 = db.child("NODE1").child("id").get().val()
    luongmua1 = db.child("NODE1").child("luong mua").get().val()
    kinhdo1 = db.child("NODE1").child("kinh do").get().val()
    vido1 = db.child("NODE1").child("vi do").get().val()
    trangthai1 = db.child("NODE1").child("trang thai").get().val()
    benngoai2 = db.child("NODE2").child("ben ngoai").get().val()
    bentrong2 = db.child("NODE2").child("ben trong").get().val()
    id2 = db.child("NODE2").child("id").get().val()
    luongmua2 = db.child("NODE2").child("luong mua").get().val()
    kinhdo2 = db.child("NODE2").child("kinh do").get().val()
    vido2 = db.child("NODE2").child("vi do").get().val()
    trangthai2 = db.child("NODE2").child("trang thai").get().val()
    if bentrong1 is None:
        bentrong1=0
    if bentrong2 is None:
        bentrong2=0
    if benngoai1 is None:
        benngoai1=0
    if benngoai2 is None:
        benngoai2=0
    if  id1 is None:
        id1=0
    if id2 is None:
        id2=0
    if luongmua1 is None:
        luongmua1=0
    if luongmua2 is None:
        luongmua2=0
    if kinhdo1 is None:
        kinhdo1=0
    if kinhdo2 is None:
        kinhdo2=0
    if vido1 is None:
        vido1=0
    if vido2 is None:
        vido2=0
    if trangthai1 is None:
        trangthai1=0
    if trangthai2 is None:
        trangthai2=0

    if trangthai1 == 1:
        tt1 = "M???"
    else: tt1="????ng"
    if trangthai2 == 1:
        tt2 = "M???"
    else: tt2="????ng"
    m = folium.Map(location=[(kinhdo1+kinhdo2)/2, (vido1+vido2)/2], zoom_start=17)
    html1 = f"""
                <h1> {"C???ng 1"}</h1>

                    <li>ID:{id1}</li>
                    <li>N???p c???ng: {tt1}</li>
                    <li>B??n ngo??i: {benngoai1} cm</li>
                    <li>B??n trong: {bentrong1} cm</li>
                    <li>L?????ng m??a: {luongmua1} mm</li>
                    <li>Vi tr??: {kinhdo1} , {vido1}</li>  
                </p>
                """
    iframe1 = folium.IFrame(html=html1, width=200, height=200)
    popup1 = folium.Popup(iframe1, max_width=2650)
    html2 = f"""
                    <h1> {"C???ng 2"}</h1>

                        <li>ID:{id2} </li>
                        <li>N???p c???ng: {tt2}</li>
                        <li>B??n ngo??i: {benngoai2} cm</li>
                        <li>B??n trong: {bentrong2} cm</li>
                        <li>L?????ng m??a: {luongmua2} cm</li>
                        <li>Vi tr??: {kinhdo2} , {vido2}</li>  
                    </p>
                    """
    if bentrong1 >30:
        html3 = f"""
               <a  href="/"><img src="https://thuviendohoa.vn/upload/images/items/logo-than-trong-bieu-tuong-canh-bao-tam-giac-vang-dau-cham-than-png-382.webp" width="80px" ,="" height="80px"></a><b> M???c n?????c trong c???ng 1 qu?? ng?????ng </b>
                
                       """
    if bentrong1 <=30:
        html3 = f""" """
    if bentrong2 > 30:
        html4 = f"""
                  <a  href="/"><img src="https://thuviendohoa.vn/upload/images/items/logo-than-trong-bieu-tuong-canh-bao-tam-giac-vang-dau-cham-than-png-382.webp" width="80px" ,="" height="80px"></a><b> M???c n?????c trong c???ng 2 qu?? ng?????ng </b>
                
                       """
    if bentrong2 <= 30:
        html4 = f""" """

    iframe2 = folium.IFrame(html=html2, width=200, height=200)
    popup2 = folium.Popup(iframe2, max_width=2650)
    if  bentrong1 < 10:
        mau1='blue'
    if 15<= bentrong1 < 25:
        mau1='green'
    if bentrong1 >= 30 :
        mau1='red'
    if  bentrong2 < 10:
        mau2='blue'
    if 15<= bentrong2 < 25:
        mau2='green'
    if benngoai2 >= 30 :
        mau2='red'

    NODE1 = folium.Marker(
        location=[kinhdo1, vido1],
        icon=folium.Icon(color=mau1, icon='fas fa-tint', prefix='fa'),
        popup=popup1,
        tooltip="NODE1")
    NODE1.add_to(m)

    NODE2 = folium.Marker(
        location=[kinhdo2, vido2],
        icon=folium.Icon(color=mau2, icon='fas fa-tint', prefix='fa'),
        popup=popup2,
        tooltip="NODE2")
    NODE2.add_to(m)
    #get Html Representation of map object
    m = m._repr_html_()

    context = {
        'm' : m,
        'n' :html3,
        'h': html4,

    }
    return render(request, 'index.html', context)
# Create your views here.