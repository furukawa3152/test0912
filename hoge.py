class Stage:
    def __init__(self, stage, quota, min, max):
        self.stage = stage  # 何ステージ目かを定義
        self.quota = quota  # ステージのクリアノルマが何問かを定義
        self.minimum = min  # ランダムで出てくる整数の最小値を定義
        self.maximum = max  # ランダムで出てくる整数の最大値を定義

    def __repr__(self):
        stage = "ステージ{}です。{}から{}の足し算だよ。{}問正解でクリア。頑張って！！".format(self.stage, self.minimum, self.maximum, self.quota)
        return stage


stage1 = Stage(1, 5, 1, 5)
stage2 = Stage(2, 5, 1, 10)
stage3 = Stage(3, 5, 1, 13)
stage_list = [stage1, stage2, stage3]


class Game:

    def __init__(self, stages):
        self.stages = stages
        self.total_score = 0
        # self.ans_count=1

    def set_stage(self, cnt):
        print(self.stages[cnt])  # ステージ stage です。 min から max の足し算だよ。 quota 問正解でクリア。頑張って！！
        min = int(self.stages[cnt].minimum)
        max = int(self.stages[cnt].maximum)
        quota = int(self.stages[cnt].quota)
        # ans_count = 1


    def play_game(self):
        import time
        import random
        stage_count = 0
        self.set_stage(stage_count)
        ans_count = 1
        print(input("10秒間に何問正解できるかな？ENTERキーでスタート！"))
        start_time = time.time()  # 解答開始時間
        while True:
            print(self.stages[stage_count])  # ステージ stage です。 min から max の足し算だよ。 quota 問正解でクリア。頑張って！！
            min = int(play.stages[stage_count].minimum)
            max = int(play.stages[stage_count].maximum)
            quota = int(play.stages[stage_count].quota)

            a = random.randint(min, max)
            b = random.randint(min, max)
            c = random.randint(min, max)
            before_time = time.time()  # この問題の出題時間。スコア作成にのみ使用。
            print(a, "+", b, "+", c, "=?")
            x = int(input())
            after_time = time.time()  # 答えた時間。
            if after_time - start_time >= 10:  # 答えた時間がスタート時間より10（秒）以上だとそこで終了。
                print("TIME UP 終了～！", ans_count - 1, "問正解でした。SCORE:", int(self.total_score), "点")
                if ans_count < quota:  # Stageクラスで定義した問題数に達しているか判定。
                    print("残念。お疲れ様でした。")
                    break
                else:
                    print("ステージクリア！！")
                    stage_count += 1
                    ans_count = 1
                    start_time = time.time()  # 解答開始時間
                    if stage_count > 3:
                        break
                    continue

            elif not (a + b + c) == x:
                print("不正解。残念！！", ans_count - 1, "問正解でした。SCORE:", int(self.total_score), "点")
                print("お疲れ様でした。")
                break
            else:
                print("正解！！", ans_count, "問正解")
                partial_score = (10 - (after_time - before_time)) * 5  # 10引く解答にかかった時間の５倍がその問題のスコアとなる。
            ans_count = ans_count + 1
            self.total_score = self.total_score + partial_score


play = Game(stage_list)  # 現状は、ここの数字を1～3で自分で変更して開始。ここを改良したい！
play.play_game()