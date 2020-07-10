from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.


class SkillStack(models.Model):
    # 스택 이름
    name = models.CharField(max_length=50, primary_key=True)
    # 스택 이미지
    img = ProcessedImageField(upload_to='icon',
                              processors=[ResizeToFill(500, 500)],
                              format='JPEG',
                              options={'quality': 60},
                              default="icon/dummy.png")
    # 스택 설명
    detail = models.TextField(null=True)
    # 스택 쉐어 링크
    stackshareLink = models.CharField(max_length=100, null=True)
    # 스택 공식 웹페이지
    webpage = models.CharField(max_length=50, null=True)
    # 카테고리 - 에러나면 에러났다는 메세지 저장
    category = models.CharField(max_length=50, null=True)
    # 생성일
    created_at = models.DateTimeField(auto_now_add=True)


class Recruit(models.Model):
    # 공고 타이틀
    title = models.CharField(max_length=50)
    # 모집 직종
    carear = models.CharField(max_length=50)
    # 원하는 경력 몇년 이상
    carear_start = models.IntegerField()
    # 원하는 경력 몇년 이하
    carear_end = models.IntegerField()
    # 모집 페이지
    recruit_page = models.CharField(max_length=200)
    # 그 사이트에서의 인덱스
    index = models.IntegerField()
    # 공고가 올라온 사이트
    site = models.CharField(max_length=50)
    # 데이터 베이스에 공고가 올라온 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 원하는 기술 스택
    # wants_stacks = models.ManyToManyField(SkillStack, related_name='wants_stacks')
    wants_stacks = models.ManyToManyField(
        SkillStack, related_name='posted_recruit')
    # uploed = models.TimeField(auto_now=True)
    # company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Company(models.Model):
    # 회사명
    name = models.CharField(max_length=50)
    # 회사 규묘(인원)
    scale = models.IntegerField()
    # 회사 위치
    location = models.CharField(max_length=60)
    # 회사 홈페이지
    homepage = models.CharField(max_length=50)
    # 이 데이터 생성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 게시한 공고
    posted_recruit = models.ManyToManyField(
        Recruit, related_name='posting_company')


# Create your models here.
class CountIssue(models.Model):
    javascript = models.CharField(max_length=20)
    java = models.CharField(max_length=20)
    python = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    csharp = models.CharField(max_length=20)
    cplus = models.CharField(max_length=20)
    go = models.CharField(max_length=20)
    ruby = models.CharField(max_length=20)
    typescript = models.CharField(max_length=20)
    php = models.CharField(max_length=20)
    scala = models.CharField(max_length=20)
    rust = models.CharField(max_length=20)
    kotlin = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    shell = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)


class CountRepository(models.Model):
    javascript = models.CharField(max_length=20)
    java = models.CharField(max_length=20)
    python = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    csharp = models.CharField(max_length=20)
    cplus = models.CharField(max_length=20)
    go = models.CharField(max_length=20)
    ruby = models.CharField(max_length=20)
    typescript = models.CharField(max_length=20)
    php = models.CharField(max_length=20)
    scala = models.CharField(max_length=20)
    rust = models.CharField(max_length=20)
    kotlin = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    shell = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)