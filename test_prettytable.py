from prettytable import PrettyTable

s = PrettyTable()

s.field_names = ["Должность", "Отдел", "Фамилия, имя", "Зарплата"]
s.add_row(["Начальник", "Отдел кадров", "Петров Сергей", 70000])
s.add_row(["Начальник", "Финансовый отдел", "Смирнова Полина", 70000])
s.add_row(["Начальник", "Отдел продаж", "Кузнецов Семен", 80000])
s.add_row(["Заместитель начальника", "Отдел кадров", "Панина Елена", 60000])
s.add_row(["Заместитель начальника", "Финансовый отдел", "Попов Сергей", 60000])
s.add_row(["Заместитель начальника", "Отдел продаж", "Дубов Дмитрий", 72000])
