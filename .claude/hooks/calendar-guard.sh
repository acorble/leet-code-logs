#!/bin/bash
# Google Calendar の操作をメインカレンダー (nob2325@gmail.com) だけに固定する PreToolUse フック。
# - calendarId は省略 / "primary" / メインのアドレスのみ許可
# - suggest_time の attendeeEmails もメインのアドレスのみ許可
# - 研究室カレンダーのアドレスは入力のどこに出てきても拒否
jq -c '
  def main: . == "primary" or . == "nob2325@gmail.com";
  (.tool_input // {}) as $in
  | [
      (if ($in | tostring | ascii_downcase | contains("nanosat.nuae@gmail.com"))
       then "研究室カレンダー (nanosat.nuae@gmail.com) は参照・編集しない設定です" else empty end),
      (($in.calendarId // "primary" | ascii_downcase) as $c
       | if ($c | main) then empty
         else "calendarId \"\($c)\" はメインカレンダーではありません（省略するか primary を使ってください）" end),
      (($in.attendeeEmails // []) | map(ascii_downcase) | map(select(main | not))
       | if length > 0 then "attendeeEmails にメインカレンダー以外が含まれています: \(join(", "))" else empty end)
    ]
  | select(length > 0)
  | {hookSpecificOutput: {hookEventName: "PreToolUse", permissionDecision: "deny",
       permissionDecisionReason: (join(" / ") + "。このリポジトリではメインカレンダーのみ操作できます")}}
'
