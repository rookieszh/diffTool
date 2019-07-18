// OverView
// ========
//  This is the clock_check module
//     ��ģ�����òο�ʱ�Ӷ�ϵͳʱ�ӽ��м�⣬�Ըߵ�ƽ�͵�
// ��ƽ�ֱ������������ֵ����ĳһֵ������Ϊϵͳʱ�Ӷ�ʧ��Ƶ�ʱ��(���Ҳ�ɼ��)��
//     ���ڲο�ʱ��Ҳ������100M������Ƶ�ʣ����Բ��ò��������룬�Բ�ͬ��ֵ�ֱ�ȡ��ͬ�Ĳ�����
// �ڶ˿ڽ������롣

//`include "xxxxx"
`timescale 1ns/100ps

module  clock_check(
        input            I_reset_n           ,  // ��λ�ź�
        input            I_reference_clk     ,  // �ο�ʱ��
        input [4:0]      I_clock_parameter   ,  // ���ϵͳʱ�Ӳ���
        input            I_clock             ,  // �����ϵͳʱ��
        output           O_clock_lose           // ָʾϵͳʱ�Ӷ�ʧ��Ƶ�ʱ��

        );


reg  [2:0] R_div1         ;
reg  [4:0] R_high_counter0;
reg  [4:0] R_low_counter0 ;
reg  [4:0] R_counter      ;
wire       W_clock_lose   ;

// ʱ��8��Ƶ
always @(posedge I_clock or negedge I_reset_n) begin
   if (~I_reset_n) begin
      R_div1 <=3'b0;
      end
   else begin
      R_div1 <=R_div1+1;
      end
   end

assign  W_div_clock1 = R_div1[2];

// �òο�ʱ�Ӽ���ϵͳʱ�ӵ��쳣���
// �о���ʽ��
// ��R_high_counter0,R_low_counter0ÿ���ڼ�����>I_clock_parameter���ϣ������ʱ��Ƶ�ʱ�ͣ�
// ��R_high_counter0,R_low_counter0ÿ���ڼ���һ��>I_clock_parameter���ϣ�һ��<I_clock_parameter-3�����ʱ�Ӷ�ʧ��
// ��R_high_counter0,R_low_counter0ÿ���ڼ�����<I_clock_parameter-3�������ʱ��Ƶ�ʱ�ߣ�
// Ŀǰֻ���ж϶�ʧ
always @(posedge I_reference_clk or negedge I_reset_n) begin
   if (~I_reset_n) begin
      R_high_counter0 <=5'b0;
      R_low_counter0  <=5'b0;
      end
   else if (W_div_clock1) begin
      R_high_counter0 <= (&R_high_counter0) ? R_high_counter0 : (R_high_counter0+1);
      R_low_counter0  <=5'b0;
      end
   else begin
      R_low_counter0  <= (&R_low_counter0) ? R_low_counter0 : (R_low_counter0 +1);
      R_high_counter0 <=5'b0;
      end
   end

assign W_clock_lose =R_high_counter0>I_clock_parameter | R_low_counter0>I_clock_parameter;
// �˶γ�������I_reference_clk��ʧ��W_div_clock1����ʧʱ�󱨣�������һ����ʱ���ϱ�
always @(posedge I_reference_clk or negedge I_reset_n) begin
   if (~I_reset_n) begin
      R_counter <=5'b0;
      end
   else if (W_clock_lose) begin
      R_counter <=(&R_counter) ? R_counter : (R_counter+1);
      end
   else begin
      R_counter <=5'b0;
      end
   end

assign O_clock_lose = R_counter>I_clock_parameter;

endmodule
