from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
import calendar

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'

    id = Column('id', Integer, primary_key=True)
    task = Column('task', String, default='There is a task')
    deadline = Column('deadline', Date, default=datetime.today())

    def __repr__(self):
        return self.task


class ToDoList:
    def __init__(self):
        self.engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        self.date = str(datetime.today().date())
        self.dates_list = None
        self.task_ordered = None
        self.tasks = None
        self.session = None
        self.user_input = None

    def main(self):

        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
        while True:
            self.tasks = self.session.query(Table).all()
            self.task_ordered = self.session.query(Table).order_by(Table.deadline).all()
            self.dates_list = [task.deadline for task in self.task_ordered]

            self.user_input = int(input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""))
            if self.user_input == 1:
                self.today_tasks()
            if self.user_input == 2:
                self.week_tasks()
            if self.user_input == 3:
                self.all_tasks()
            if self.user_input == 4:
                self.missed_tasks()
            if self.user_input == 5:
                self.input_tasks()
            if self.user_input == 6:
                self.delete_tasks()
            if self.user_input == 0:
                print()
                print("Bye!")
                break

    def print_tasks_one_by_one(self, dates=None, flag=True):
        if dates is None:
            dates = [datetime.today().date()]
        for date in dates:
            today = date.day if date.day > 9 else f'0{date.day}'
            if flag:
                print(f'\nToday: {today} {date.strftime("%b")}')
            else:
                print(f'\n{calendar.day_name[date.weekday()]}: {today} {date.strftime("%b")}')
            tasks = [task for task in self.tasks if str(task.deadline) == str(date)]
            if len(tasks) == 0:
                print("Nothing to do!")
            else:
                counter = 0
                for task in tasks:
                    counter += 1
                    print(f'{counter}. {task}')
        print()

    def print_all_tasks(self, tasks, date):
        for i in range(len(tasks)):
            print(f'{i + 1}. {tasks[i]}. {date[i].day} {date[i].strftime("%b")}')

    def input_tasks(self):
        daily_task = input("\nEnter task\n")
        deadline = datetime.strptime(input("Enter deadline\n"), '%Y-%m-%d')
        new_row = Table(task=daily_task, deadline=deadline)
        print("The task has been added\n")
        self.session.add(new_row)
        self.session.commit()

    def today_tasks(self):
        print()
        self.print_tasks_one_by_one()

    def week_tasks(self):
        print()
        deadline = [datetime.today().date() + timedelta(days=i) for i in range(7)]
        self.print_tasks_one_by_one(deadline, False)

    def all_tasks(self):
        print("\nAll tasks: ")
        self.print_all_tasks(self.task_ordered, self.dates_list)
        print()

    def missed_tasks(self):
        print("\nMissed tasks:")
        rows = self.session.query(Table).filter(Table.deadline < datetime.today().date()).all()
        dates = [task.deadline for task in rows]
        self.print_all_tasks(rows, dates)
        print()

    def delete_tasks(self):
        print("\nChoose the number of the task you want to delete:")
        self.print_all_tasks(self.task_ordered, self.dates_list)
        id_list = [task.id for task in self.task_ordered]
        task_id = id_list[int(input()) - 1]
        if id is None:
            print("Nothing to delete")
        else:
            self.session.query(Table).filter(Table.id == task_id).delete()
            self.session.commit()
        print()


todo = ToDoList()
todo.main()
