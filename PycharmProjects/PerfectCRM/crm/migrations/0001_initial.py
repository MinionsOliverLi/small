# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('addr', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': '校区',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(0, '面授(脱产)'), (1, '面授(周末)'), (2, '网络班')], verbose_name='班级类型')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('end_date', models.DateField(blank=True, verbose_name='结业日期', null=True)),
                ('branch', models.ForeignKey(to='crm.Branch', verbose_name='校区')),
            ],
            options={
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('period', models.PositiveSmallIntegerField(verbose_name='周期(月)')),
                ('outline', models.TextField()),
            ],
            options={
                'verbose_name_plural': '课程表',
            },
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='第几节(天)')),
                ('has_homework', models.BooleanField(default=True)),
                ('homework_title', models.CharField(max_length=128, blank=True, null=True)),
                ('homework_content', models.TextField(blank=True, null=True)),
                ('outline', models.TextField(verbose_name='本节课程大纲')),
                ('date', models.DateField(auto_now_add=True)),
                ('from_class', models.ForeignKey(to='crm.ClassList', verbose_name='班级')),
            ],
            options={
                'verbose_name_plural': '上课记录',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, blank=True, null=True)),
                ('qq', models.CharField(max_length=64, unique=True)),
                ('qq_name', models.CharField(max_length=64, blank=True, null=True)),
                ('phone', models.CharField(max_length=64, blank=True, null=True)),
                ('source', models.SmallIntegerField(choices=[(0, '转介绍'), (1, 'QQ群'), (2, '官网'), (3, '百度推广'), (4, '51CTO'), (5, '知乎'), (6, '市场推广')])),
                ('referral_from', models.CharField(max_length=64, blank=True, verbose_name='转介绍人qq', null=True)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '已报名'), (1, '未报名')])),
                ('content', models.TextField(verbose_name='咨询详情')),
                ('memo', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consult_course', models.ForeignKey(to='crm.Course', verbose_name='咨询课程')),
            ],
            options={
                'verbose_name_plural': '客户表',
            },
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('content', models.TextField(verbose_name='跟进内容')),
                ('intention', models.SmallIntegerField(choices=[(0, '2周内报名'), (1, '1个月内报名'), (2, '近期无报名计划'), (3, '已在其它机构报名'), (4, '已报名'), (5, '已拉黑')])),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '客户跟进记录',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(default=False, verbose_name='学员已同意合同条款')),
                ('contract_approved', models.BooleanField(default=False, verbose_name='合同已审核')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '报名表',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': '菜单',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=500, verbose_name='数额')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '缴费记录',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('attendance', models.SmallIntegerField(default=0, choices=[(0, '已签到'), (1, '迟到'), (2, '缺勤'), (3, '早退')])),
                ('score', models.SmallIntegerField(default=0, choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (-100, 'COPY'), (0, 'N/A')])),
                ('memo', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('course_record', models.ForeignKey(to='crm.CourseRecord')),
                ('student', models.ForeignKey(to='crm.Enrollment')),
            ],
            options={
                'verbose_name_plural': '学习记录',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('menus', models.ManyToManyField(to='crm.Menu', blank=True, null=True)),
                ('roles', models.ManyToManyField(to='crm.Role', blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '账号表',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='consultant',
            field=models.ForeignKey(to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(to='crm.Course', verbose_name='所报课程'),
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='consultant',
            field=models.ForeignKey(to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='customer',
            field=models.ForeignKey(to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrolled_class',
            field=models.ForeignKey(to='crm.ClassList', verbose_name='所报班级'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='consultant',
            field=models.ForeignKey(to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(to='crm.Tag', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(to='crm.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('student', 'course_record')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('customer', 'enrolled_class')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('from_class', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'course', 'semester')]),
        ),
    ]
