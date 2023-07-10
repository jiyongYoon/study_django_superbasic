from django.apps import AppConfig

# 해당 클래스 파일은 앱 생성시 자동으로 만들어지므로 따로 만들 필요는 없음.


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # primary_key 속성을 설정함
    name = 'pybo' # 앱의 이름 명시
