//
//  CourseManager.m
//  Qcumber
//
//  Created by Chris Cooper on 11-10-12.
//  Copyright 2011 Chris Cooper. All rights reserved.
//

#import "CourseManager.h"

static CourseManager *_course_manager_instance = nil;

@implementation CourseManager

+(CourseManager*)sharedInstance {
    if (_course_manager_instance == nil) {
        _course_manager_instance = [[CourseManager alloc] init];
    }
    
    return _course_manager_instance;
}

- (id)init
{
    self = [super init];
    if (self) {
        // Initialization code here.
    }
    
    return self;
}

@end
