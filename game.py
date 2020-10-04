import time
import random


class Stage:
    def __init__(self, stage, quota, min, max):
        self.stage = stage  # 何ステージ目かを定義
        self.quota = quota  # ステージのクリアノルマが何問かを定義
        self.minimum = min  # ランダムで出てくる整数の最小値を定義
        self.maximum = max  # ランダムで出てくる整数の最大値を定義

    def __repr__(self):
        stage = "ステージ{}です。{}から{}の足し算だよ。{}問正解でクリア。頑張って！！".format(self.stage, self.minimum, self.maximum, self.quota)
        return stage


class Timer:

    def __init__(self):
        self.start_time = 0
        self.before_time = 0
        self.after_time = 0

    def set_start(self):
        self.start_time = time.time()

    def set_before(self):
        self.before_time = time.time()

    def set_after(self):
        self.after_time = time.time()

    def judge_timeup(self, ans_count: int, total_score: int):  # 答えた時間がスタート時間より10（秒）以上だとそこで終了。
        if self.after_time - self.start_time >= 10:
            print("TIME UP 終了～！", ans_count - 1, "問正解でした。SCORE:", int(total_score), "点")
            return True


class Game:

    def __init__(self, stages):
        self.stages = stages
        self.timer = Timer()
        self.total_score = 0
        self.partial_score = 0
        self.stage_count = -1
        self.ans_count = 0
        self.range_min = 0
        self.range_max = 0
        self.quota = 0

    def set_stage(self):
        print(self.stages[self.stage_count])  # ステージ stage です。 min から max の足し算だよ。 quota 問正解でクリア。頑張って！！
        self.ans_count = 1
        self.range_min = int(self.stages[self.stage_count].minimum)
        self.range_max = int(self.stages[self.stage_count].maximum)
        self.quota = int(self.stages[self.stage_count].quota)
        print(input("10秒間に何問正解できるかな？ENTERキーでスタート！"))
        self.timer.set_start()

    def judge_ansewr(self, correct_answer: int, input_answer: int):
        if input_answer != correct_answer:
            print("不正解。残念！！", self.ans_count - 1, "問正解でした。SCORE:", int(self.total_score), "点")
            print("お疲れ様でした。")
            return False

        print("正解！！", self.ans_count, "問正解")
        partial_score = (10 - (self.timer.after_time - self.timer.before_time)) * 5
        self.total_score += partial_score
        self.ans_count += 1
        return True

    def judge_clear(self):  # Stageクラスで定義した問題数に達しているか判定。

        if self.ans_count <= self.quota:
            print("残念。お疲れ様でした。")
            return False
        else:
            print("ステージクリア！！")
        if self.stage_count < 2:
            self.stage_count += 1
            self.set_stage()
            return True
        else:
            print("全ステージクリアです！おめでとう！！")
            return False

    def play_game(self):
        # import time
        # import random

        while self.stage_count < 0 or self.stage_count > 2:
            print("ステージ1～3を数字で選択してね")
            self.stage_count = int(input()) - 1
            continue
        self.set_stage()

        while True:
            a = random.randint(self.range_min, self.range_max)
            b = random.randint(self.range_min, self.range_max)
            c = random.randint(self.range_min, self.range_max)
            correct_answer = a + b + c
            self.timer.set_before()  # この問題の出題時間。スコア作成にのみ使用。

            print(a, "+", b, "+", c, "=?")
            try:
                input_answer = int(input())
            except ValueError:
                print("数字を入力してね")
                continue
            self.timer.set_after()  # 答えた時間。

            if self.timer.judge_timeup(self.ans_count, self.total_score):
                if not self.judge_clear():
                    break
                else:
                    continue
            else:
                if not self.judge_ansewr(correct_answer, input_answer):  # 答えの判定
                    break


if __name__ == "__main__":
    stage1 = Stage(1, 5, 1, 5)
    stage2 = Stage(2, 5, 1, 10)
    stage3 = Stage(3, 5, 1, 13)
    stage_list = [stage1, stage2, stage3]
    play = Game(stage_list)
    play.play_game()
