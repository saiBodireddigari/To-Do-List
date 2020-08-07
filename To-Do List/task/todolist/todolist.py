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

            self.user_input = int(input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
"""))
            if self.user_input == 1:
                self.today_tasks()
            if self.user_input == 2:
                self.week_tasks()
            if self.user_input == 3:
                self.all_tasks()
            if self.user_input == 4:
                self.input_tasks()
            if self.user_input == 0:
                print()
                print("Bye!")
                break

    def print_tasks(self, dates=None, flag=True):
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

    def input_tasks(self):
        daily_task = input("\nEnter task\n")
        deadline = datetime.strptime(input("Enter deadline\n"), '%Y-%m-%d')
        new_row = Table(task=daily_task, deadline=deadline)
        print("The task has been added\n")
        self.session.add(new_row)
        self.session.commit()

    def today_tasks(self):
        print()
        self.print_tasks()

    def week_tasks(self):
        print()
        deadline = [datetime.today().date()+timedelta(days=i) for i in range(7)]
        self.print_tasks(deadline, False)

    def all_tasks(self):
        print("\nAll tasks: ")
        tasks = [task for task in self.task_ordered]
        date = [task.deadline for task in self.task_ordered]
        for i in range(len(tasks)):
            print(f'{i+1}. {tasks[i]}. {date[i].day} {date[i].strftime("%b")}')
        print()


todo = ToDoList()
todo.main()
