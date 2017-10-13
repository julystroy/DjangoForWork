insert into 01u_0base (`uid`,
`time_h`,
`guid`,
`un`,
`uname`,
`bindname`,
`cid`,
`pass`,
`salt`,
`flag`,
`uc_id`,
`paypass`,
`old_pass`,
`old_encrystr_login`,
`is_old`,
`errmm_num`,
`errmm_last`,
`openid`,
`access_token`,
`expire_time`,
`utype`,
`isvaild`,
`validdate`
) select `uid`,
`time_h`,
`guid`,
`un`,
`uname`,
`bindname`,
`cid`,
`pass`,
`salt`,
`flag`,
`uc_id`,
`paypass`,
`old_pass`,
`old_encrystr_login`,
`is_old`,
`errmm_num`,
`errmm_last`,
`openid`,
`access_token`,
`expire_time`,
`utype`,
`isvaild`,
`validdate` from wd.01u_0base
WHERE time_h > DATE_FORMAT(DATE_SUB(curdate(),INTERVAL 1 DAY),"%Y-%m-%d 23:30:00") and time_h <= DATE_FORMAT(curdate(),"%Y-%m-%d 23:30:00");
