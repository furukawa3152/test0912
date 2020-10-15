def punch_out(left: int, right: int, hp: int) -> int:
    import binary_search

    max_count_left = hp // left  # 左で最大何発殴れるか
    max_count_right = hp // right  # 右で最大何発殴れるか
    # 左で殴った場合のダメージリスト作成
    left_attack_damage = [0]
    for i in range(1, max_count_left + 1):
        left_attack_damage.append(left * i)

    # 右で殴った場合のダメージリスト作成
    right_attack_damage = [0]
    for j in range(1, max_count_right + 1):
        right_attack_damage.append(right * j)

    # 右で殴った場合のダメージリストの値を使って、左で殴った場合のダメージリストを探索
    min_count = hp
    for j in range(1, max_count_right + 1):
        target = hp - right_attack_damage[j]
        i = binary_search.b_search(tbl=left_attack_damage, in_num=target)
        if min_count > i + j:
            min_count = i + j

    return min_count


if __name__ == "__main__":
    L,R = map(int, input().split())
    HP = int(input())
    print(punch_out(left=L, right=R, hp=HP))