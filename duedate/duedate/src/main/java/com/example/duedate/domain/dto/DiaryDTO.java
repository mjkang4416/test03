package com.example.duedate.domain.dto;

import lombok.Data;

@Data
public class DiaryDTO {
    private long diaryId;
    private long userNumber;
    private String diaryDate;
    private String diaryTitle;
    private String diaryEmo;
    private String diaryContent;

}
