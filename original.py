def fullbokko(L,R,N):
    L_punch = 0#常にL<Rなので、Lが最小のケースから試していき、N-LがRで割り切れたらそこで終了。
    while True:
        if N % R == 0:
            break
        else:
            N-=L
            L_punch += 1#Rが割り切れる数が登場するまでLを増やし続ける。
    return int(L_punch+N/R)

L,R=map(int,input().split())
N=int(input())
print(fullbokko(L,R,N))


# l, r = map(int, input().split())
# hp = int(input())
#
# # 右と左の最大のパンチの回数（割り算の切り上げ）
# left_max = -(-hp // l)
# right_max = -(-hp // r)
#
# # hpと、右と左の合計が等しくなる数字を入れるリスト。
# total_punch_list = []
#
# # 左右のパンチのダメージがちょうどhpになるすべての組み合わせ（左右を合計した数字）をリストに入れる。
# for i in range(left_max + 1):
#     for j in range(right_max + 1):
#         if i * l + j * r == hp:
#             tmp = i + j
#             total_punch_list.append(tmp)
#
# # リスト（パンチの回数）の最少を出す。
# ans = min(total_punch_list)
# print(ans)
#
# l, r = map(int, input().split())
# hp = int(input())
#
# left_max = -(-hp // l)
# right_max = -(-hp // r)
#
#
# for i in range(left_max + 1):
#     for j in range(right_max + 1):
#         if i * l + j * r == hp:
#             print(i + j)
#             exit()

#
# def punch_out(left: int, right: int, hp: int) -> int:
#     import binary_search
#
#     max_count_left = hp // left  # 左で最大何発殴れるか
#     max_count_right = hp // right  # 右で最大何発殴れるか
#     # 左で殴った場合のダメージリスト作成
#     left_attack_damage = [0]
#     for i in range(1, max_count_left + 1):
#         left_attack_damage.append(left * i)
#
#     # 右で殴った場合のダメージリスト作成
#     right_attack_damage = [0]
#     for j in range(1, max_count_right + 1):
#         right_attack_damage.append(right * j)
#
#     # 右で殴った場合のダメージリストの値を使って、左で殴った場合のダメージリストを探索
#     min_count = hp
#     for j in range(1, max_count_right + 1):
#         target = hp - right_attack_damage[j]
#         i = binary_search.b_search(tbl=left_attack_damage, in_num=target)
#         if min_count > i + j:
#             min_count = i + j
#
#     return min_count
#
#
# if __name__ == "__main__":
#     L, R = map(int, input().split())
#     HP = int(input())
#     print(punch_out(left=L, right=R, hp=HP))
