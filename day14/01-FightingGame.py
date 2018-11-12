class Player(object):
  """玩家"""
  def __init__(self, name):
    self.name = name
    self.hp = 100 # 玩家血量
    self.gun = None

  def __str__(self):
    if self.gun == None:
      return "%s 剩余血量为 %d, 目前没有枪" % (self.name, self.hp)
    else:
      return "%s 剩余血量为 %d, 枪的信息: %s" % (self.name, self.hp, self.gun)

  def zhuangZiDan(self, box, bullet):
    """拿起弹夹安装子弹"""
    box.fill(bullet)

  def zhuangDanJia(self, gun, box):
    """拿起枪，装弹夹"""
    gun.load(box)

  def takeGun(self, gun):
    if not self.gun:
      self.gun = gun
    else:
      print("已经有枪了，不能再拿了...")

  def kouBanJi(self, enemy):
    self.gun.fire(enemy)

  def dropHp(self, power):
    self.hp -= power
    if self.hp <= 0:
      print("啊，我死了...")


class Gun(object):
  """枪"""
  def __init__(self, name):
    self.name = name
    self.box = None

  def load(self, box):
    if not self.box:
      self.box = box
    else:
      print("枪里已经有弹夹了...")

  def  __str__(self):
    if not self.box:
      return "%s没有弹夹" % self.name
    else:
      return "%s的弹夹是: %s" % (self.name, self.box)

  def fire(self, enemy):
    """射击敌人"""
    # 取子弹
    bullet = self.box.pop()

    # 射击子弹
    if bullet != None:
      bullet.hurt(enemy)


class Box(object):
  """弹夹"""
  def __init__(self, maxNum):
    self.bullets = []
    self.maxNum = maxNum

  def fill(self, bullet):
    if len(self.bullets) < self.maxNum:
      self.bullets.append(bullet)
    else:
      print("弹夹已满，无法继续安装子弹...")

  def __str__(self):
    return "弹夹容量为: %d ，弹夹里子弹有 %d 颗子弹" % (self.maxNum, len(self.bullets))

  def pop(self):
    if len(self.bullets) > 0:
      bullet = self.bullets.pop()
      return bullet
    else:
      print("子弹已用完,请重新装填子弹...")
      return


class Bullet(object):
  """子弹"""
  def __init__(self, power):
    self.power = power

  def hurt(self, enemy):
    enemy.dropHp(self.power)


# 创建老王
laowang = Player('老王')
print(laowang)

# 准备枪支弹药
# 准备枪
gun = Gun('AK47')
print(gun)

# 准备子弹
bullet = Bullet(57)

# 准备弹夹
box = Box(20)
print(box)

# 把子弹安装到弹夹里
laowang.zhuangZiDan(box, bullet)
print(box)

# 把弹夹安装到枪里面
laowang.zhuangDanJia(gun, box)
print(gun)

# box2 = Box()
# laowang.zhuangDanJia(gun, box2)
# print(gun)

# 拿起枪
laowang.takeGun(gun)
print(laowang)
print('==================枪已备好，静待午时==================')

# 创建敌人
enemy = Player('敌人')
print(enemy)

# 射击敌人
laowang.kouBanJi(enemy)
print(enemy)

laowang.kouBanJi(enemy)
print(enemy)

bullet1 = Bullet(57)
bullet2 = Bullet(57)
laowang.zhuangZiDan(box, bullet1)
print(laowang)
laowang.zhuangZiDan(box, bullet2)
print(laowang)
laowang.kouBanJi(enemy)
print(enemy)
laowang.kouBanJi(enemy)
print(enemy)
